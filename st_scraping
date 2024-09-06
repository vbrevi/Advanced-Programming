# Auto detect text files and perform LF normalization
from bs4 import BeautifulSoup
import requests
import csv

# Base URL of the site for book pages
base_url = "https://books.toscrape.com/catalogue/page-{}.html"
book_base_url = "https://books.toscrape.com/catalogue/"

# List to store the details of all the books
books = []

# Loop to navigate through all the pages (1-50)
for page_num in range(1, 51):
    # Generate the URL for the current page
    url = base_url.format(page_num)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all book containers on the page
    articles = soup.find_all('article', class_='product_pod')
    
    # Extract information from each book
    for article in articles:
        # Find the link to the book
        book_link = article.h3.a['href']
        full_book_link = book_base_url + book_link
        
        # Go to the specific book page
        book_response = requests.get(full_book_link)
        book_soup = BeautifulSoup(book_response.text, 'html.parser')
        
        # Extract book details
        title = book_soup.h1.text
        price = book_soup.find('p', class_='price_color').text
        availability = book_soup.find('p', class_='instock availability').text.strip()
        
        # Extract the genre
        genre = book_soup.find('ul', class_='breadcrumb').find_all('li')[2].text.strip()

        # Extract the rating
        rating = book_soup.find('p', class_='star-rating')['class'][1]
        rating_dict = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5
        }
        rating_value = rating_dict.get(rating, 'N/A')

        # Extract the description
        description_tag = book_soup.find('div', id='product_description')
        if description_tag:
            description = description_tag.find_next_sibling('p').text.strip()
        else:
            description = "No description available"

        # UPC, Type, Price excl. tax, Price incl. tax, Tax, Availability, Number of reviews
        product_info_table = book_soup.find('table', class_='table table-striped')
        product_info = {}
        for row in product_info_table.find_all('tr'):
            heading = row.th.text
            value = row.td.text
            product_info[heading] = value
        
        upc = product_info.get('UPC', 'N/A')
        product_type = product_info.get('Product Type', 'N/A')
        price_excl_tax = product_info.get('Price (excl. tax)', 'N/A')
        price_incl_tax = product_info.get('Price (incl. tax)', 'N/A')
        tax = product_info.get('Tax', 'N/A')
        number_of_reviews = product_info.get('Number of reviews', 'N/A')
        
        # Add book information to the list
        books.append([
            title, price, availability, genre, rating_value, description, upc, 
            product_type, price_excl_tax, price_incl_tax, tax, number_of_reviews
        ])

# Save all data to a CSV file
with open('books_info.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow([
        'Title', 'Price', 'Availability', 'Genre', 'Rating', 
        'Description', 'UPC', 'Product Type', 
        'Price (excl. tax)', 'Price (incl. tax)', 'Tax', 
        'Number of Reviews'
    ])
    # Write the data of each book
    writer.writerows(books)

print("Book information has been saved to books_info.csv")

