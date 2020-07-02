# -*- coding: utf-8 -*-
"""
Practice code to find all books in a fictional online book store with a particular Star rating using Beautiful Soup and Requests modules in Python
Website used for scraping:  toscrape.com (books section)
"""


import bs4
import requests

store_url = 'http://books.toscrape.com/catalogue/page-{}.html'
# format the store url for each page as store_url.format(page_no)


'''

There are 1000 total items across 50 pages. We will use a while loop to iterate across the 50 pages.

All required tags etc are found out by inspecting elements and viewing page source of the target site beforehand

Basic format for web-scraping:
    
    res = requests.get('target_url')            returns the page source html code of the website at 'target_url' as a raw Python string
    soup = bs4.BeautifulSoup(res.text, 'lxml')  parses the above obtained string into a more usable format
    soup.select('required_tag')                 returns as a list-esque object containing dictionary-esque elements with required_tag in them
                                                    use . prefix if searching for a class with the name required_tag
                                                    use # prefix if searching for an id with the name required_tag
    soup.select('required_tag')[index][Key]     returns the value assigned for that particular 'Key' in a particular element in the above list
                                                    can be used to find the source url of an image in the website using 'src' for key and appropriate values for the other fields

'''

num_keys = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five"}


def anystar_scraper(num):
    titles = []
    star_rating = ".star-rating.{}"                                     #first dot to signify it's a class, second dot to signify the presence of space
    for i in range(20):
        res = requests.get(store_url.format(i+1))
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        products = soup.select('.product_pod')
        for product in products:
            if [] != product.select(star_rating.format(num_keys[num])):    
                titles.append(product.select('a')[1]['title'])
                pass
    
    print(f"{len(titles)} Books found with {num} Star rating:")
    input("Press Enter to display the book titles.")        
    for title in titles:
        print(title)
        
def driver_fn():
    print("Books-to-Scrape Web Scraper v1.0")
    input("Press Enter to Continue.")
    while True:
        cont_choice=''
        num=0
        while True:
            try:
                num = int(input("Enter the star rating you are looking for as an integer [1-5]:"))
            except:
                print("Whoops! Invalid entry. Please enter a suitable integer between 1 and 5. Try again!")
                continue
            else:
                if num in range(1,6):
                    break
                else:
                    print("Whoops! Invalid entry. Please enter a suitable integer between 1 and 5. Try again!")
                    continue
        print("Processing. This may take a few moments...")
        anystar_scraper(num)
        while True:
            cont_choice = input("Do you wish to check out books of any other rating? [Y/N]:")
            if cont_choice.lower()=='y' or cont_choice.lower()=='n':
                break
            else:
                print("Whoops! Invalid entry. Please enter 'Y' for Yes or 'N' for No. Try again!")
                continue
        if cont_choice.lower()=='y':
            continue
        else:
            break
    print("End of web-scraping script.")
    input("Press Enter to Continue.")
    
    
driver_fn()
