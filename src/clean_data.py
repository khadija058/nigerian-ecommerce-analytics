import pandas as pd
import numpy as np
import os

def load_raw_data():
    """Load the raw data"""
    print("📖 Loading raw data...")
    
    file_path = 'data/raw/nigerian_ecommerce_sample.csv'
    df = pd.read_csv(file_path)
    
    print(f"✅ Loaded {len(df)} records")
    return df

def clean_data(df):
    """Clean and enhance the data"""
    print("\n🧹 Starting data cleaning process...")
    
    # Make a copy
    df_clean = df.copy()
    original_shape = df_clean.shape
    
    print(f"📊 Original data: {original_shape[0]} rows, {original_shape[1]} columns")
    
    # Step 1: Convert dates
    print("\n🔧 Step 1: Converting dates...")
    df_clean['order_date'] = pd.to_datetime(df_clean['order_date'])
    print("✅ Dates converted to datetime format")
    
    # Step 2: Create derived features
    print("\n🔧 Step 2: Creating derived features...")
    
    # Calculate total sales if not exists
    if 'total_sales' not in df_clean.columns:
        df_clean['total_sales'] = df_clean['quantity'] * df_clean['unit_price']
    
    # Date features
    df_clean['year'] = df_clean['order_date'].dt.year
    df_clean['month'] = df_clean['order_date'].dt.month
    df_clean['day_of_week'] = df_clean['order_date'].dt.dayofweek
    df_clean['is_weekend'] = df_clean['day_of_week'].isin([5, 6])
    
    # Business features
    df_clean['price_category'] = pd.cut(df_clean['unit_price'], 
                                       bins=[0, 50000, 200000, 500000, float('inf')],
                                       labels=['Low', 'Medium', 'High', 'Premium'])
    
    print("✅ Created date and business features")
    
    # Step 3: Data validation
    print("\n🔧 Step 3: Data validation...")
    
    # Check for negative values
    negative_prices = (df_clean['unit_price'] < 0).sum()
    negative_quantities = (df_clean['quantity'] < 0).sum()
    
    print(f"  Negative prices: {negative_prices}")
    print(f"  Negative quantities: {negative_quantities}")
    
    # Remove any negative values
    df_clean = df_clean[(df_clean['unit_price'] > 0) & (df_clean['quantity'] > 0)]
    
    # Step 4: Text cleaning
    print("\n�� Step 4: Text cleaning...")
    
    text_columns = ['customer_name', 'product_name', 'category', 'state', 'city']
    for col in text_columns:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].str.strip().str.title()
    
    print("✅ Text data cleaned and standardized")
    
    # Final summary
    final_shape = df_clean.shape
    print(f"\n🎉 Data cleaning complete!")
    print(f"📊 Final data: {final_shape[0]} rows, {final_shape[1]} columns")
    print(f"📈 Columns added: {final_shape[1] - original_shape[1]}")
    
    return df_clean

def save_cleaned_data(df_clean):
    """Save cleaned data"""
    print("\n�� Saving cleaned data...")
    
    # Create processed data directory
    os.makedirs('data/processed', exist_ok=True)
    
    # Save to CSV
    output_path = 'data/processed/cleaned_data.csv'
    df_clean.to_csv(output_path, index=False)
    
    print(f"✅ Cleaned data saved to: {output_path}")
    return output_path

def data_quality_report(df_clean):
    """Generate data quality report"""
    print("\n" + "="*50)
    print("📋 DATA QUALITY REPORT")
    print("="*50)
    
    print(f"📊 Dataset Shape: {df_clean.shape}")
    print(f"🔍 Missing Values: {df_clean.isnull().sum().sum()}")
    print(f"📋 Duplicates: {df_clean.duplicated().sum()}")
    
    print(f"\n📈 Numerical Summary:")
    numerical_cols = ['quantity', 'unit_price', 'total_sales']
    for col in numerical_cols:
        if col in df_clean.columns:
            print(f"  {col}:")
            print(f"    Min: {df_clean[col].min():,}")
            print(f"    Max: {df_clean[col].max():,}")
            print(f"    Mean: {df_clean[col].mean():,.2f}")
    
    print(f"\n📅 Date Range: {df_clean['order_date'].min()} to {df_clean['order_date'].max()}")
    
    print(f"\n🏷️ Categories:")
    for col in ['category', 'state', 'price_category']:
        if col in df_clean.columns:
            print(f"  {col}: {df_clean[col].nunique()} unique values")

if __name__ == "__main__":
    print("🚀 Nigerian E-Commerce Data Cleaning Pipeline")
    print("-" * 48)
    
    # Load raw data
    df_raw = load_raw_data()
    
    # Clean the data
    df_clean = clean_data(df_raw)
    
    # Save cleaned data
    save_cleaned_data(df_clean)
    
    # Generate quality report
    data_quality_report(df_clean)
    
    print("\n✨ Data cleaning pipeline completed successfully!")
