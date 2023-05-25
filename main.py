import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
import time


num_pages = 20


base_url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2 C283&ref=sr_pg_1'


params = {
    'k': 'bags',
    'crid': '2M096C61O4MLT',
    'qid': '1653308124',
    'sprefix': 'ba%2Caps%2C283',
    'ref': 'sr_pg_'
}


csv_file = open('scraped_data.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product URL', 'Product Name', 'Product Price', 'Rating', 'Number of Reviews', 'Description', 'ASIN', 'Product Description', 'Manufacturer'])


for page in range(1, num_pages+1):
 
    params['ref'] = f'sr_pg_{page}'


    response = requests.get(base_url, params=params)

  
    soup = BeautifulSoup(response.content, 'html.parser')

   
    product_containers = soup.find_all('div', {'data-component-type': 's-search-result'})

 
    for container in product_containers:
       
        product_url = container.find('a', {'class': 'a-link-normal s-no-outline'})['href']

       
        if not product_url.startswith('http'):
            product_url = urljoin(base_url, product_url)

      
        product_name = container.find('span', {'class': 'a-size-medium a-color-base a-text-normal'}).text.strip()

     
        product_price = container.find('span', {'class': 'a-offscreen'}).text.strip()

       
        rating = container.find('span', {'class': 'a-icon-alt'}).text.strip()

      
        num_reviews = container.find('span', {'class': 'a-size-base'}).text.strip()

    
        product_response = requests.get(product_url)

       
        product_soup = BeautifulSoup(product_response.content, 'html.parser')

      
        description_element = product_soup.find('div', {'id': 'productDescription'})
        description = description_element.text.strip() if description_element else ''

        asin_element = product_soup.find('th', text='ASIN')
        asin = asin_element.find_next('td').text.strip() if asin_element else ''

        product_description_element = product_soup.find('div', {'id': 'productDescription'})
        product_description = product_description_element.text.strip() if product_description_element else ''

        manufacturer_element = product_soup.find('th', text='Manufacturer')
        manufacturer = manufacturer_element.find_next('td').text.strip() if manufacturer_element else ''

       
        csv_writer.writerow([product_url, product_name, product_price, rating, num_reviews, description, asin, product_description, manufacturer])

    
    time.sleep(2)


csv_file.close()
