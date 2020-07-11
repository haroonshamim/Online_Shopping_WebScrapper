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
        driver.get('https://homeshopping.pk/search.php?q={}'.format(query.replace(' ', '%20')))
        time.sleep(5)
        page_source=driver.page_source;
        link = BeautifulSoup(page_source, 'html.parser').find('div', class_='product-box')
        urlList = [atag['href'] for atag in link]

        print(urlList[1])
        mobile_url = requests.get(urlList[1],
                                 headers=my_headers).text
        name = ((BeautifulSoup(mobile_url, 'html.parser').find('div', class_="productname").text))
        price = ((BeautifulSoup(mobile_url, 'html.parser').find('div', class_="ActualPrice").text))
        print(name)
        return price


def main():
    price = WhatmobileScraper().getFirstResultPrice(query=input(' Enter Smart-phone name: '))
    print('Price:', price)

if __name__ == '__main__':
    main()