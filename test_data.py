import pandas as pd

try:
    # Try to load the Excel file
    df = pd.read_excel('Nigerian ECommerce Dataset.xlsx')
    print("Success! File loaded.")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
except FileNotFoundError:
    print("Excel file not found. Please check the file name and location.")
except ImportError as e:
    print(f"Missing package: {e}")
except Exception as e:
    print(f"Error: {e}")
