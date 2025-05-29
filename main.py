from etl.extract import extract_books

def run_etl():
    
    books = extract_books()
    print(books.head())
    print(f"Total books scraped: {len(books)}")

if __name__ == "__main__":
    run_etl()
