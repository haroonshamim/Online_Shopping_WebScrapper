import requests
from bs4 import BeautifulSoup
import re


my_headers = {}
my_headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'




class WhatmobileScraper:
    # Returns the price of the first result of search query given
    def getFirstResultPrice(self, query='mobile'):

        response_text = requests.get('https://www.whatmobile.com.pk/search.php?q={}'.format(query.replace(' ', '+')), headers=my_headers).text
        # now reponse_text is holding all source code of above link

        try:
            # now when we search the mobile always the first searched up item is our required result so we only want 1st link
            first_result_url = 'https://www.whatmobile.com.pk{}'.format(BeautifulSoup(response_text, 'html.parser').find('a', class_='BiggerText')['href'])

            actual_phone_source=requests.get(first_result_url,headers=my_headers).text
            #.text means inner text data mean data having
            price_text=BeautifulSoup(actual_phone_source,'html.parser').find('div', class_='hdng3').text

            if 'Discontinued' in price_text:
                return None
            print(price_text)
             #our string is this  Rs. 59, 999 USD $447
            # the re means that string containing Rs followed by . here we wrote \. because . is a special character
            # to just use. as character we use \
            #[0-9,]+ mean our sting may contain any number and comma of any quantities
            pkr_price = float(re.findall('Rs\. ([0-9,]+) ', price_text)[0].replace(',', ''))

            return pkr_price
        except:
            return "Item not found "




######
######
######

def main():
    price = WhatmobileScraper().getFirstResultPrice(query=input(' Enter Smart-phone name: '))
    print('Price:', price)

if __name__ == '__main__':
    main()