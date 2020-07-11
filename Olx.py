import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from selenium import webdriver
import time
import json
my_headers = {}
my_headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

class WhatmobileScraper:

    def getFirstResultPrice(self, query='mobile'):


        driver = webdriver.Chrome()
        driver.get('https://www.olx.com.pk/lahore_g4060673/q-{}'.format(query.replace(' ', '-')))
        time.sleep(5)
        page_source=driver.page_source;
        data = BeautifulSoup(page_source, 'html.parser').find_all(class_='EIR5N')

        # so as there are 20 items so we have 20 length list . Each index hold information about one item
        #print(len(data))

        #productName=data[0].find('span',class_='_2tW1I').text
        productPrice=[]
        productName=[]

        for x in data:

            productPrice.append ((x.find('span',class_='_89yzn').text))
            productName.append(x.find('span',class_='_2tW1I').text)

        Infomation = {
            'Product_Title': productName,
            'Price': productPrice,
        }
        x=len(productName)
        z=0
        while(z<x):
            print(productName[z]+","+productPrice[z])
            z=z+1;





def main():
    price = WhatmobileScraper().getFirstResultPrice(query=input(' Enter Smart-phone name: '))


if __name__ == '__main__':
    main()