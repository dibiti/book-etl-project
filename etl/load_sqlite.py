import sqlite3
import os

def load_books_to_sqlite(df, db_path='data/books.db', table_name='books'):
    """
    Load a pandas DataFrame into a SQLite database table.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be saved.
    - db_path (str): Path to the SQLite database file.
    - table_name (str): Name of the table where data will be inserted.
    """
    # Make sure the data folder exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Connect to the SQLite database (creates it if it doesn't exist)
    conn = sqlite3.connect(db_path)

    # Load the DataFrame into the database (replaces the table if it exists)
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print(f"✅ Data successfully saved to SQLite database: {db_path}, table: {table_name}")
