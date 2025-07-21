import pandas as pd
import numpy as np
from datetime import datetime
import os

print("🚀 Nigerian E-Commerce ETL Pipeline")
print("=" * 60)

# STEP 1: EXTRACT
print("\n📥 STEP 1: EXTRACTING DATA...")
try:
    df = pd.read_excel('Nigerian E-Commerce Dataset.xlsx')
    print("✅ Data extracted from current directory")
except FileNotFoundError:
    try:
        df = pd.read_excel('data/Nigerian E-Commerce Dataset.xlsx')
        print("✅ Data extracted from data directory")
    except FileNotFoundError:
        print("❌ File not found in either location")
        exit()

print(f"📊 Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns")

# STEP 2: TRANSFORM
print("\n🔄 STEP 2: TRANSFORMING DATA...")
df_clean = df.copy()
df_clean['Order Date'] = pd.to_datetime(df_clean['Order Date'])
print("✅ Data transformation completed")

# STEP 3: ANALYZE
print("\n📈 STEP 3: BUSINESS ANALYTICS...")
total_revenue = df_clean['Total Price'].sum()
total_orders = df_clean['Order ID'].nunique()
avg_order_value = total_revenue / total_orders

print(f"\n💰 BUSINESS METRICS:")
print(f"   Total Revenue: ₦{total_revenue:,.2f}")
print(f"   Total Orders: {total_orders:,}")
print(f"   Average Order Value: ₦{avg_order_value:,.2f}")

print(f"\n🎉 ETL PIPELINE COMPLETED!")
# STEP 4: ADVANCED ANALYTICS
print("\n📊 STEP 4: ADVANCED ANALYTICS...")

# Monthly trends
print("\n📅 MONTHLY PERFORMANCE:")
monthly_revenue = df_clean.groupby(df_clean['Order Date'].dt.month)['Total Price'].sum()
for month, revenue in monthly_revenue.items():
    month_name = pd.to_datetime(f'2023-{month:02d}-01').strftime('%B')
    print(f"   {month_name}: ₦{revenue:,.2f}")

# Regional analysis
print(f"\n🌍 REGIONAL BREAKDOWN:")
regional_stats = df_clean.groupby('Order Region').agg({
    'Total Price': ['sum', 'mean', 'count'],
    'Quantity': 'sum'
}).round(2)

for region in df_clean['Order Region'].unique()[:10]:  # Top 10 regions
    region_data = df_clean[df_clean['Order Region'] == region]
    total_rev = region_data['Total Price'].sum()
    avg_order = region_data['Total Price'].mean()
    orders_count = len(region_data)
    print(f"   {region}: ₦{total_rev:,.0f} total, ₦{avg_order:,.0f} avg, {orders_count} orders")

# Product categories analysis
print(f"\n🏷️ TOP PERFORMING ITEMS:")
item_performance = df_clean.groupby('Item Name').agg({
    'Quantity': 'sum',
    'Total Price': 'sum'
}).sort_values('Total Price', ascending=False).head(10)

for item, data in item_performance.iterrows():
    print(f"   {item}: {data['Quantity']:,} units, ₦{data['Total Price']:,.0f}")

# Business insights
print(f"\n💡 KEY INSIGHTS:")
top_region = df_clean.groupby('Order Region')['Total Price'].sum().idxmax()
top_product = df_clean.groupby('Item Name')['Quantity'].sum().idxmax()
busiest_month = monthly_revenue.idxmax()

print(f"   • Strongest market: {top_region}")
print(f"   • Best-selling product: {top_product}")
print(f"   • Peak sales month: {pd.to_datetime(f'2023-{busiest_month:02d}-01').strftime('%B')}")
print(f"   • Average items per order: {df_clean['Quantity'].mean():.1f}")