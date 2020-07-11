import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from selenium import webdriver
import time
import json

my_headers = {}
my_headers[
    'user-agent'] = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'


class WhatmobileScraper:

    def getFirstResultPrice(self, query='mobile'):

        driver = webdriver.Chrome()
        driver.get('https://www.amazon.com/s?k={}'.format(query.replace(' ', '+')))
        time.sleep(5)
        page_source = driver.page_source;

        # There are two types of Items. One having price and one having no price. So data 2 conatins div of no price items
        # but still some items in div 2 have price so that is why i am using try and except

        data = BeautifulSoup(page_source, 'html.parser').find_all('div',
                                                                  class_="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 AdHolder sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28")
        data2 = BeautifulSoup(page_source, 'html.parser').find_all('div',
                                                                   class_="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28")

        for x in data:
            try:
                print(x.find('span', class_='a-size-medium a-color-base a-text-normal').text)
                print(x.find('span', class_='a-offscreen').text)
            except:
                print("Item not found in X")

        for y in data2:
            try:

                print(y.find('span', class_='a-size-medium a-color-base a-text-normal').text)
                print(y.find('span', class_='a-offscreen').text)
            except:
                print('No Price Mentioned')


def main():
    price = WhatmobileScraper().getFirstResultPrice(query=input(' Enter Item name: '))


if __name__ == '__main__':
    main()