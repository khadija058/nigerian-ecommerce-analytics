import pandas as pd
import numpy as np

print("Loading Nigerian E-Commerce Dataset...")

try:
    # Load the exact filename from your upload
    df = pd.read_excel('Nigerian E-Commerce Dataset.xlsx')
    print("✅ Successfully loaded the dataset!")
    
    print("\n=== DATASET OVERVIEW ===")
    print(f"Shape: {df.shape} (rows, columns)")
    print(f"\nColumns:")
    for i, col in enumerate(df.columns):
        print(f"{i+1}. {col}")
    
    print(f"\nFirst 3 rows:")
    print(df.head(3))
    
    print(f"\nData types:")
    print(df.dtypes)
    
    print(f"\nMissing values:")
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print(missing[missing > 0])
    else:
        print("No missing values!")
    
    print(f"\nBasic statistics for numeric columns:")
    print(df.describe())
    
except Exception as e:
    print(f"❌ Error: {e}")

