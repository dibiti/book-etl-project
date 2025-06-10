import os

def load_books(df, output_path='data/books.csv'):
    """
    Save the cleaned book data into a CSV file.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing transformed book data.
    - output_path (str): The destination path for the CSV file.
    """
    # Create the /data folder if it does not exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the DataFrame as a CSV file
    df.to_csv(output_path, index=False)
    print(f"✅ Data saved successfully to: {output_path}")
