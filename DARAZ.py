from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions




class DarazScraper:
	# Returns the price of the first result of search query given
	def getFirstResultPrice(self, query='mobile'):
		chrome_options = ChromeOptions()
		chrome_options.add_argument('--headless')
		driver = webdriver.Chrome('./chromedriver', options=chrome_options)
		driver.get('https://www.daraz.pk/catalog/?q={}'.format(query.replace(' ', '+')))
		first_product_div = driver.find_element_by_class_name('c2prKC')
		product_title = first_product_div.find_element_by_class_name('c16H9d').get_attribute('innerText')
		pkr_price = first_product_div.find_element_by_class_name('c3gUW0').get_attribute('innerText')
		driver.quit()
		return pkr_price




######
######
######

def main():
	price = DarazScraper().getFirstResultPrice(query=input(' Enter Smart-phone name: '))
	print('Price:', price)

if __name__ == '__main__':
	main()