from etl.extract import extract_books
from etl.transform import transform_books
from etl.load import load_books

def run_etl():
    
    books = extract_books()
    #print(books.head())
    #print(f"Total books scraped: {len(books)}")

    df_clean = transform_books(books)
    #print(df_clean.dtypes)
    #print(df_clean.head())

    load_books(df_clean)

if __name__ == "__main__":
    run_etl()
