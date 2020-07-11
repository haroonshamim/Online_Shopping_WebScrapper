import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from selenium import webdriver
import time

my_headers = {}
my_headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

class WhatmobileScraper:

    def getFirstResultPrice(self, query='mobile'):


        driver = webdriver.Chrome()
        driver.get('https://www.telemart.pk/search?query={}'.format(query.replace(' ', '+')))
        time.sleep(5)
        page_source=driver.page_source;
        link=BeautifulSoup(page_source, 'html.parser').find('div', class_='ais-Hits').find('a')['href']

        response_text = requests.get(link,
                                 headers=my_headers).text
        name = ((BeautifulSoup(response_text, 'html.parser').find('h3', class_='product-title').text))
        price=((BeautifulSoup(response_text, 'html.parser').find('span', id='pprice').text))
        print(name)

def main():
    price = WhatmobileScraper().getFirstResultPrice(query=input(' Enter Smart-phone name: '))
    print('Price:', price)

if __name__ == '__main__':
    main()