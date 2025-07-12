import pandas as pd
import os
import urllib.request
import zipfile

def download_sample_data():
    """Download sample e-commerce data for analysis"""
    print("📥 Setting up sample Nigerian e-commerce data...")
    
    # Create sample data since we don't have Kaggle set up yet
    sample_data = {
        'order_id': ['ORD001', 'ORD002', 'ORD003', 'ORD004', 'ORD005', 'ORD006'],
        'customer_id': ['CUST001', 'CUST002', 'CUST001', 'CUST003', 'CUST002', 'CUST004'],
        'customer_name': ['Ahmed Lagos', 'Fatima Abuja', 'Ahmed Lagos', 'Kemi Ibadan', 'Fatima Abuja', 'Chidi Enugu'],
        'product_name': ['Samsung Phone', 'HP Laptop', 'Phone Charger', 'Apple iPad', 'Dell Monitor', 'iPhone 13'],
        'category': ['Electronics', 'Computers', 'Accessories', 'Tablets', 'Computers', 'Electronics'],
        'quantity': [1, 1, 2, 1, 1, 1],
        'unit_price': [150000, 450000, 5000, 320000, 180000, 580000],
        'order_date': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19', '2024-01-20'],
        'state': ['Lagos', 'Abuja', 'Lagos', 'Oyo', 'Abuja', 'Enugu'],
        'city': ['Lagos', 'Abuja', 'Lagos', 'Ibadan', 'Abuja', 'Enugu']
    }
    
    # Create DataFrame
    df = pd.DataFrame(sample_data)
    
    # Save to CSV
    os.makedirs('data/raw', exist_ok=True)
    df.to_csv('data/raw/nigerian_ecommerce_sample.csv', index=False)
    
    print(f"✅ Sample data created: {len(df)} records")
    print(f"📊 Columns: {list(df.columns)}")
    
    return df

def load_data():
    """Load the data for analysis"""
    print("📖 Loading data...")
    
    file_path = 'data/raw/nigerian_ecommerce_sample.csv'
    
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print(f"✅ Loaded {len(df)} records")
        print("\n👀 First 3 rows:")
        print(df.head(3))
        print(f"\n📋 Data types:")
        print(df.dtypes)
        return df
    else:
        print("❌ Data file not found")
        return None

def preview_data(df):
    """Preview the data"""
    if df is not None:
        print("\n" + "="*50)
        print("📊 DATA PREVIEW")
        print("="*50)
        
        print(f"📈 Dataset Shape: {df.shape}")
        print(f"📅 Date Range: {df['order_date'].min()} to {df['order_date'].max()}")
        print(f"💰 Total Sales: ₦{(df['quantity'] * df['unit_price']).sum():,}")
        print(f"👥 Unique Customers: {df['customer_id'].nunique()}")
        print(f"🛍️ Unique Products: {df['product_name'].nunique()}")
        
        print(f"\n🏆 Top Products:")
        product_sales = (df.groupby('product_name')['quantity'] * 
                        df.groupby('product_name')['unit_price']).sum().sort_values(ascending=False)
        for i, (product, sales) in enumerate(product_sales.head(3).items(), 1):
            print(f"  {i}. {product}: ₦{sales:,}")

if __name__ == "__main__":
    print("🚀 Nigerian E-Commerce Data Extraction")
    print("-" * 40)
    
    # Download/create sample data
    df = download_sample_data()
    
    # Load data
    df = load_data()
    
    # Preview data
    preview_data(df)
    
    print("\n🎉 Data extraction complete!")
    print("📁 Data saved to: data/raw/nigerian_ecommerce_sample.csv")
