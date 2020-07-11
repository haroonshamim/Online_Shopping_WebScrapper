import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from selenium import webdriver
import time
import webbrowser
class Scrapper:
    def __init__(self):
        self.my_headers = {}
        self.my_headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

        self.item_name=input(' Enter Item  Name : ')
        print("Searching Your Websites. It will take 15-30 seconds")
        self.scrap()
        self.Ishopping()
        self.Homeshopping()
        self.Telemart()
        self.WhatMobile()
        self.Daraz()
        self.printprices()
        self.open=input("Enter the name of website (eg.'Ishopping') from which you want to purchase "+self.item_name+" \nor \nEnter 'Exit' :")
        if(open!="Exit"):
            print("Opening Website")
            self.openwebsite()
    def scrap(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome('./chromedriver', options=self.chrome_options)
    def Ishopping(self):
        self.driver.get('https://www.ishopping.pk/search/?q={}'.format(self.item_name.replace(' ', '+')))
        time.sleep(5)
        self.page_source = self.driver.page_source;
        self.link = BeautifulSoup(self.page_source, 'html.parser').find('div', class_='klevuImgWrap').find('a')['href']

        self.mobile_url = requests.get(self.link, headers=self.my_headers).text
        self.Ishopping_url=self.link
        self.Ishopping_name = ((BeautifulSoup(self.mobile_url, 'html.parser').find('div', class_="product-name").text)).replace('\n', ' ')
        self.Ishopping_price = ((BeautifulSoup(self.mobile_url, 'html.parser').find(class_="price").text))
        return self.Ishopping_price
    def Homeshopping(self):
        self.driver.get('https://homeshopping.pk/search.php?q={}'.format(self.item_name.replace(' ', '%20')))
        time.sleep(5)
        self.page_source = self.driver.page_source;
        self.link = BeautifulSoup(self.page_source, 'html.parser').find('div', class_='product-box')
        urlList = [atag['href'] for atag in self.link]
        self.Homeshopping_url = urlList[1]
        mobile_url = requests.get(urlList[1],
                                  headers=self.my_headers).text
        self.Homeshopping_name = ((BeautifulSoup(mobile_url, 'html.parser').find('div', class_="productname").text))
        self.Homeshopping_price = ((BeautifulSoup(mobile_url, 'html.parser').find('div', class_="ActualPrice").text))
        return self.Homeshopping_price
    def Telemart(self):
        self.driver.get('https://www.telemart.pk/search?query={}'.format(self.item_name.replace(' ', '+')))
        time.sleep(5)
        self.page_source = self.driver.page_source;
        link = BeautifulSoup(self.page_source, 'html.parser').find('div', class_='ais-Hits').find('a')['href']
        self.Telemart_url = link
        response_text = requests.get(link,
                                     headers=self.my_headers).text
        self.Telemart_name = ((BeautifulSoup(response_text, 'html.parser').find('h3', class_='product-title').text))
        self.Telemart_price = ((BeautifulSoup(response_text, 'html.parser').find('span', id='pprice').text))
        return self.Telemart_price
    def WhatMobile(self):
        try:
            response_text = requests.get(
                'https://www.whatmobile.com.pk/search.php?q={}'.format(self.item_name.replace(' ', '+')),
                headers=self.my_headers).text
            # now when we search the mobile always the first searched up item is our required result so we only want 1st link
            first_result_url = 'https://www.whatmobile.com.pk{}'.format(BeautifulSoup(response_text, 'html.parser').find('a', class_='BiggerText')['href'])
            self.WhatMobile_url = first_result_url
            actual_phone_source=requests.get(first_result_url,headers=self.my_headers).text
            #.text means inner text data mean data having


            self.WhatMobile_name = BeautifulSoup(actual_phone_source, 'html.parser').find('h1', class_='hdng3').text
            price_text=BeautifulSoup(actual_phone_source,'html.parser').find('div', class_='hdng3').text

            if 'Discontinued' in price_text:
                return None

             #our string is this  Rs. 59, 999 USD $447
            # the re means that string containing Rs followed by . here we wrote \. because . is a special character
            # to just use. as character we use \
            #[0-9,]+ mean our sting may contain any number and comma of any quantities
            self.Whatmobile_price = float(re.findall('Rs\. ([0-9,]+) ', price_text)[0].replace(',', ''))


        except:
            self.Whatmobile_price= "Item not found "
    def Daraz(self):
        self.driver.get('https://www.daraz.pk/catalog/?q={}'.format(self.item_name.replace(' ', '+')))
        first_product_div = self.driver.find_element_by_class_name('c2prKC')
        self.Daraz_name = first_product_div.find_element_by_class_name('c16H9d').get_attribute('innerText')
        self.Daraz_price = first_product_div.find_element_by_class_name('c3gUW0').get_attribute('innerText')

    def printprices(self):
         print("Price of "+self.Ishopping_name+" On Ishopping Website is "+self.Ishopping())
         print("Price of " + self.Homeshopping_name + " On Homeshopping Website is " + self.Homeshopping_price)
         print("Price of " + self.Telemart_name + " On TeleMart Website is " + self.Telemart_price)
         if(self.Whatmobile_price !="Item not found "):
            print("Price of " + self.WhatMobile_name + " On WhatMobile Website is RS." + str(self.Whatmobile_price))
         print("Price of " + self.Daraz_name + " On Daraz Website is " + self.Daraz_price)
            

    def displaylinks(self):
        print("Links are given below :")
        print(self.Ishopping_url)
        print(self.Homeshopping_url)
        print(self.Telemart_url)
        print(self.WhatMobile_url)
    def openwebsite(self):
        if(self.open  == 'Homeshopping'):
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
            webbrowser.get('chrome').open(self.Homeshopping_url)
        if (self.open == 'Ishopping'):
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
            webbrowser.get('chrome').open(self.Ishopping_url)
        if (self.open == 'TeleMart'):
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
            webbrowser.get('chrome').open(self.Telemart_url)
        if (self.open == 'WhatMobile'):
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
            webbrowser.get('chrome').open(self.WhatMobile_url)

demo=Scrapper()
