import pandas as pd
import matplotlib.pyplot as plt
import os

print("🎨 Creating Simple Colored Charts...")

# Load data
df = pd.read_excel('data/Nigerian E-Commerce Dataset.xlsx')
df['Order Date'] = pd.to_datetime(df['Order Date'])

os.makedirs('visualizations', exist_ok=True)

# Simple color scheme
colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c', '#34495e', '#e67e22']

# Create individual charts (less complex = fewer errors)

# 1. Monthly Revenue - Simple Line Chart
plt.figure(figsize=(12, 6))
monthly_data = df.groupby(df['Order Date'].dt.month)['Total Price'].sum()
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
months_in_data = [month_names[i-1] for i in monthly_data.index]

plt.plot(months_in_data, monthly_data.values, marker='o', linewidth=3, 
         markersize=8, color='#e74c3c', markerfacecolor='#3498db')
plt.title('Monthly Revenue Trend', fontsize=16, fontweight='bold')
plt.ylabel('Revenue (₦)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('visualizations/monthly_revenue_clean.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Top Regions - Colorful Bars
plt.figure(figsize=(12, 6))
top_regions = df.groupby('Order Region')['Total Price'].sum().sort_values(ascending=False).head(8)
bars = plt.bar(range(len(top_regions)), top_regions.values, color=colors[:len(top_regions)])
plt.title('Top Regions by Revenue', fontsize=16, fontweight='bold')
plt.ylabel('Revenue (₦)', fontsize=12)
plt.xticks(range(len(top_regions)), top_regions.index, rotation=45, ha='right')

# Add value labels on bars
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'₦{height/1000000:.1f}M', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('visualizations/regional_revenue_clean.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Product Performance - Horizontal Bars
plt.figure(figsize=(12, 8))
top_products = df.groupby('Item Name')['Quantity'].sum().sort_values(ascending=False).head(10)
bars = plt.barh(range(len(top_products)), top_products.values, color=colors[:len(top_products)])
plt.title('Top 10 Products by Quantity Sold', fontsize=16, fontweight='bold')
plt.xlabel('Quantity Sold', fontsize=12)
plt.yticks(range(len(top_products)), top_products.index, fontsize=10)

# Add value labels
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width + 50, bar.get_y() + bar.get_height()/2.,
             f'{width:,}', ha='left', va='center', fontsize=9)

plt.tight_layout()
plt.savefig('visualizations/product_performance_clean.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Simple Pie Chart
plt.figure(figsize=(10, 8))
top_5_regions = df.groupby('Order Region')['Total Price'].sum().sort_values(ascending=False).head(5)
plt.pie(top_5_regions.values, labels=top_5_regions.index, autopct='%1.1f%%', 
        colors=colors[:5], startangle=90)
plt.title('Revenue Distribution by Top 5 Regions', fontsize=16, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.savefig('visualizations/revenue_distribution_clean.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Clean colored charts created successfully!")
print("📊 Files created:")
print("   - monthly_revenue_clean.png")
print("   - regional_revenue_clean.png") 
print("   - product_performance_clean.png")
print("   - revenue_distribution_clean.png")
