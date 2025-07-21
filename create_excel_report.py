import pandas as pd
import os

print("📊 Creating Excel Results Report...")

# Load the original data
df = pd.read_excel("data/Nigerian E-Commerce Dataset.xlsx")
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create Excel writer
excel_file = 'outputs/Nigerian_Ecommerce_Results.xlsx'
with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
    
    # Sheet 1: Raw Data Summary
    summary_data = {
        'Metric': ['Total Revenue', 'Total Orders', 'Total Items Sold', 'Average Order Value', 'Date Range'],
        'Value': [
            f"₦{df['Total Price'].sum():,.2f}",
            f"{df['Order ID'].nunique():,}",
            f"{df['Quantity'].sum():,}",
            f"₦{df['Total Price'].sum() / df['Order ID'].nunique():,.2f}",
            f"{df['Order Date'].min().strftime('%Y-%m-%d')} to {df['Order Date'].max().strftime('%Y-%m-%d')}"
        ]
    }
    pd.DataFrame(summary_data).to_excel(writer, sheet_name='Summary', index=False)
    
    # Sheet 2: Top Regions
    top_regions = df.groupby('Order Region').agg({
        'Total Price': 'sum',
        'Order ID': 'nunique',
        'Quantity': 'sum'
    }).round(2)
    top_regions.columns = ['Total_Revenue', 'Total_Orders', 'Total_Items']
    top_regions = top_regions.sort_values('Total_Revenue', ascending=False)
    top_regions.to_excel(writer, sheet_name='Regional_Performance')
    
    # Sheet 3: Product Performance
    product_performance = df.groupby('Item Name').agg({
        'Quantity': 'sum',
        'Total Price': 'sum',
        'Order ID': 'nunique'
    }).round(2)
    product_performance.columns = ['Total_Quantity', 'Total_Revenue', 'Number_of_Orders']
    product_performance = product_performance.sort_values('Total_Revenue', ascending=False)
    product_performance.to_excel(writer, sheet_name='Product_Performance')
    
    # Sheet 4: Monthly Analysis
    monthly_analysis = df.groupby(df['Order Date'].dt.month).agg({
        'Total Price': 'sum',
        'Order ID': 'nunique',
        'Quantity': 'sum'
    }).round(2)
    monthly_analysis.columns = ['Monthly_Revenue', 'Monthly_Orders', 'Monthly_Items']
    monthly_analysis.index.name = 'Month'
    monthly_analysis.to_excel(writer, sheet_name='Monthly_Trends')
    
    # Sheet 5: Cleaned Full Dataset
    df.to_excel(writer, sheet_name='Full_Dataset', index=False)

print(f"✅ Excel report created: {excel_file}")
print("📋 Sheets included:")
print("   1. Summary - Key business metrics")
print("   2. Regional_Performance - Revenue by region")
print("   3. Product_Performance - Top products analysis")
print("   4. Monthly_Trends - Time-based analysis")
print("   5. Full_Dataset - Complete cleaned data")
