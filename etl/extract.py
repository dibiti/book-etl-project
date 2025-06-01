import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_books():
    """
    Extract book data from all catalog pages of 'Books to Scrape'.

    Returns:
        pd.DataFrame: A DataFrame containing book details like title, price, stock, rating, and URL.
    """
    url_base = "http://books.toscrape.com/catalogue/page-{}.html"
    books = []

    # Iterate over all 50 catalog pages
    for page in range(1, 51):
        #print(f"Extracting page {page}...")
        url = url_base.format(page)
        res = requests.get(url)
        res.encoding = 'utf-8' 

        #Skip the page if request fails
        if res.status_code != 200:
            print(f"Failed to retrieve page {page}. Status code {res.status_code}")
            break
    soup = BeautifulSoup(res.text, 'html.parser')

    # Each book is inside an <article class="product_pod">
    articles = soup.select('article.product_pod')

    for article in articles:
        title = article.h3.a['title']
        price = article.select_one('.price_color').text
        stock = article.select_one('.availability').text.strip()
        rating = article.select_one('p')['class'][1]  # Rating is in the second class name
        relative_link = article.h3.a['href']

        # Create full URL for the book
        full_link = f"http://books.toscrape.com/catalogue/{relative_link}"

        books.append({
            'title': title,
            'price': price,
            'stock': stock,
            'rating': rating,
            'url': full_link
        })

    # Convert the list of dictionaries into a pandas DataFrame
    return pd.DataFrame(books)
        
