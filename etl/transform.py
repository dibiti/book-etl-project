import pandas as pd

def transform_books(df):
    """
    Clean and transform book data.

    Args:
        df (pd.DataFrame): Raw book data from extract phase.

    Returns:
        pd.DataFrame: Cleaned and normalized data ready for loading.
    """
    df = df.copy()

    # Remove pound sign and convert price to float
    df['price'] = df['price'].str.replace('£', '', regex=False).astype(float)

    # Extract numeric value from stock string (currently wrong, need to extract the correct number of th stock by visit each book link individually, next step)
    df['stock'] = df['stock'].str.extract(r'(\d+)').fillna(0).astype(int)

    # Convert rating words to numeric scale
    rating_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    df['rating'] = df['rating'].map(rating_map)

    return df