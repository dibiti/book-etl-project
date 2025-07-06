import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("data/books.db")

# Run a simple SQL query to see the first rows
query = "SELECT * FROM books LIMIT 5;"
df = pd.read_sql_query(query, conn)

# Get books with price > 50
expensive_books = pd.read_sql_query("SELECT title, price FROM books WHERE price > 50;", conn)
print(expensive_books)

# Count how many books have 5-star rating
rating_count = pd.read_sql_query("SELECT COUNT(*) FROM books WHERE rating = 5;", conn)
print(rating_count)


# Show the result
print(df)

# Close the connection
conn.close()
