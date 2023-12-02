import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "http://quotes.toscrape.com"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract information from the page
    quotes = []
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]

        quotes.append({
            'text': text,
            'author': author,
            'tags': ', '.join(tags)
        })

    # Save quotes to a CSV file
    filename = 'inspirational_quotes.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['text', 'author', 'tags']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        # Write the header
        writer.writeheader()

        # Write each quote to the CSV file
        for quote in quotes:
            writer.writerow(quote)

    print(f"Quotes have been successfully saved to {filename}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
