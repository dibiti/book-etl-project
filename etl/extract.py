import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/page-1.html"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# Pega os dois primeiros livros da página
books = soup.select('article.product_pod')[:2]

for book in books:
    title = book.h3.a['title']
    price = book.select_one('.price_color').text
    stock = book.select_one('.availability').text.strip()
    rating = book.select_one('p')['class'][1]  # ex: 'Three'
    print(f"Título: {title}, Preço: {price}, Estoque: {stock}, Avaliação: {rating}")
