import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("🔧 Fixing and Creating Better Visualizations...")

# Load data
df = pd.read_excel('data/Nigerian E-Commerce Dataset.xlsx')
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Set style
plt.style.use('default')
sns.set_palette("husl")

# Create output directory
os.makedirs('visualizations', exist_ok=True)

# Create a better dashboard with proper data
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Nigerian E-Commerce Analytics Dashboard (Fixed)', fontsize=16, fontweight='bold')

# 1. Monthly Revenue Trend (Fix the empty chart)
monthly_data = df.groupby(df['Order Date'].dt.month)['Total Price'].sum()
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_data.index = [month_names[i-1] for i in monthly_data.index]

axes[0,0].plot(monthly_data.index, monthly_data.values, marker='o', linewidth=3, markersize=8)
axes[0,0].set_title('Monthly Revenue Trend', fontsize=14, fontweight='bold')
axes[0,0].set_ylabel('Revenue (₦)', fontsize=12)
axes[0,0].tick_params(axis='x', rotation=45)
axes[0,0].grid(True, alpha=0.3)

# 2. Top 10 Regions (Keep this one - it's working)
top_regions = df.groupby('Order Region')['Total Price'].sum().sort_values(ascending=False).head(10)
bars = axes[0,1].bar(range(len(top_regions)), top_regions.values, color='green', alpha=0.8)
axes[0,1].set_title('Top 10 Regions by Revenue', fontsize=14, fontweight='bold')
axes[0,1].set_ylabel('Revenue (₦)', fontsize=12)
axes[0,1].set_xticks(range(len(top_regions)))
axes[0,1].set_xticklabels(top_regions.index, rotation=45, ha='right')

# 3. Regional Distribution (Fix the pie chart)
top_5_regions = df.groupby('Order Region')['Total Price'].sum().sort_values(ascending=False).head(5)
others_sum = df.groupby('Order Region')['Total Price'].sum().sort_values(ascending=False)[5:].sum()

if others_sum > 0:
    pie_data = top_5_regions.copy()
    pie_data['Others'] = others_sum
else:
    pie_data = top_5_regions

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc', '#c2c2f0']
wedges, texts, autotexts = axes[1,0].pie(pie_data.values, labels=pie_data.index, 
                                        autopct='%1.1f%%', startangle=90, colors=colors)
axes[1,0].set_title('Revenue Distribution by Region', fontsize=14, fontweight='bold')

# 4. Top Products by Quantity
top_products = df.groupby('Item Name')['Quantity'].sum().sort_values(ascending=False).head(10)
bars = axes[1,1].barh(range(len(top_products)), top_products.values, color='orange', alpha=0.8)
axes[1,1].set_title('Top 10 Products by Quantity Sold', fontsize=14, fontweight='bold')
axes[1,1].set_xlabel('Quantity Sold', fontsize=12)
axes[1,1].set_yticks(range(len(top_products)))
axes[1,1].set_yticklabels(top_products.index, fontsize=10)

plt.tight_layout()
plt.savefig('visualizations/fixed_dashboard.png', dpi=300, bbox_inches='tight')
print("✅ Fixed dashboard saved: visualizations/fixed_dashboard.png")
print("🎉 All visualizations fixed and created successfully!")
