# Amazon Product Scraper

This Python script is designed to scrape product details from multiple pages of an Amazon product listing. It retrieves information such as product URL, name, price, rating, number of reviews, description, ASIN, product description, and manufacturer.

## Features

- Scrape product details from multiple pages of an Amazon product listing
- Extract information such as URL, name, price, rating, and number of reviews
- Fetch additional details by visiting each product URL, including description, ASIN, product description, and manufacturer
- Supports scraping of up to 20 pages and 200 product URLs

## Usage

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Adjust the `num_pages` variable to specify the number of product listing pages to scrape.
3. Run the script using `python main.py`.
4. The scraped data will be exported to a CSV file named `scraped_data.csv`.

## Dependencies

- Python 3.x
- Beautiful Soup 4
- Requests

## Legal Considerations

Please note that web scraping should be done responsibly and in compliance with the terms of service of the target website. Make sure to review and respect the website's policies and rate limits when using this script.

Happy scraping!
