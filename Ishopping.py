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
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome('./chromedriver', options=chrome_options)
        driver.get('https://www.ishopping.pk/search/?q={}'.format(query.replace(' ', '+')))
        time.sleep(5)
        page_source=driver.page_source;
        link = BeautifulSoup(page_source, 'html.parser').find('div', class_='klevuImgWrap').find('a')['href']

        mobile_url = requests.get(link,headers=my_headers).text
        name=((BeautifulSoup(mobile_url, 'html.parser').find( 'div',class_="product-name").text)).replace('\n', ' ')
        price = ((BeautifulSoup(mobile_url, 'html.parser').find( class_="price").text))
        return name


def main():
    price = WhatmobileScraper().getFirstResultPrice(query=input(' Enter Smart-phone name: '))
    print('Price:', price)

if __name__ == '__main__':
    main()