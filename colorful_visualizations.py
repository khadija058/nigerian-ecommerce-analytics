import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("🎨 Creating Colorful Custom Charts...")

# Load data
df = pd.read_excel('data/Nigerian E-Commerce Dataset.xlsx')
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Custom color schemes
custom_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57', '#FF9FF3', '#54A0FF']
gradient_colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c', '#4facfe', '#00f2fe']
business_colors = ['#2c3e50', '#3498db', '#e74c3c', '#f39c12', '#27ae60', '#9b59b6']

os.makedirs('visualizations', exist_ok=True)

# Create dashboard with custom colors
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Nigerian E-Commerce Dashboard - Custom Colors', fontsize=16, fontweight='bold')

# 1. Monthly Revenue with gradient colors
monthly_data = df.groupby(df['Order Date'].dt.month)['Total Price'].sum()
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_data.index = [month_names[i-1] for i in monthly_data.index]

# Custom gradient line chart
axes[0,0].plot(monthly_data.index, monthly_data.values, 
              marker='o', linewidth=4, markersize=10, 
              color='#FF6B6B', markerfacecolor='#4ECDC4', 
              markeredgecolor='#FF6B6B', markeredgewidth=2)
axes[0,0].set_title('Monthly Revenue Trend', fontsize=14, fontweight='bold', color='#2c3e50')
axes[0,0].set_ylabel('Revenue (₦)', fontsize=12, color='#2c3e50')
axes[0,0].grid(True, alpha=0.3, color='#95a5a6')
axes[0,0].set_facecolor('#f8f9fa')

# 2. Top Regions with custom colors
top_regions = df.groupby('Order Region')['Total Price'].sum().sort_values(ascending=False).head(8)
bars = axes[0,1].bar(range(len(top_regions)), top_regions.values, 
                    color=custom_colors[:len(top_regions)], alpha=0.8, 
                    edgecolor='white', linewidth=2)
axes[0,1].set_title('Top Regions by Revenue', fontsize=14, fontweight='bold', color='#2c3e50')
axes[0,1].set_ylabel('Revenue (₦)', fontsize=12, color='#2c3e50')
axes[0,1].set_xticks(range(len(top_regions)))
axes[0,1].set_xticklabels(top_regions.index, rotation=45, ha='right')
axes[0,1].set_facecolor('#f8f9fa')

# 3. Beautiful Pie Chart with custom colors
top_5_regions = df.groupby('Order Region')['Total Price'].sum().sort_values(ascending=False).head(5)
pie_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']
wedges, texts, autotexts = axes[1,0].pie(top_5_regions.values, 
                                        labels=top_5_regions.index,
                                        autopct='%1.1f%%', 
                                        startangle=90, 
                                        colors=pie_colors,
                                        explode=(0.05, 0, 0, 0, 0),  # Explode first slice
                                        shadow=True)
axes[1,0].set_title('Revenue Distribution', fontsize=14, fontweight='bold', color='#2c3e50')

# 4. Horizontal bar with gradient
top_products = df.groupby('Item Name')['Quantity'].sum().sort_values(ascending=False).head(8)
bars = axes[1,1].barh(range(len(top_products)), top_products.values, 
                     color=gradient_colors[:len(top_products)], alpha=0.9,
                     edgecolor='white', linewidth=1)
axes[1,1].set_title('Top Products by Quantity', fontsize=14, fontweight='bold', color='#2c3e50')
axes[1,1].set_xlabel('Quantity Sold', fontsize=12, color='#2c3e50')
axes[1,1].set_yticks(range(len(top_products)))
axes[1,1].set_yticklabels(top_products.index, fontsize=10)
axes[1,1].set_facecolor('#f8f9fa')

plt.tight_layout()
plt.savefig('visualizations/colorful_dashboard.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✅ Colorful dashboard saved!")

# Create individual themed charts
print("🎨 Creating themed individual charts...")

# Business Professional Theme
plt.figure(figsize=(12, 8))
plt.style.use('seaborn-v0_8-whitegrid')
top_regions.plot(kind='bar', color=business_colors[:len(top_regions)], 
                figsize=(12, 8), alpha=0.8, edgecolor='black', linewidth=0.8)
plt.title('Regional Performance - Professional Theme', fontsize=16, fontweight='bold', pad=20)
plt.ylabel('Revenue (₦)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('visualizations/professional_theme.png', dpi=300, bbox_inches='tight')

# Vibrant/Fun Theme
plt.figure(figsize=(12, 8))
monthly_data.plot(kind='area', color='#FF6B6B', alpha=0.7, figsize=(12, 8))
plt.title('Monthly Revenue Trend - Vibrant Theme', fontsize=16, fontweight='bold', pad=20)
plt.ylabel('Revenue (₦)', fontsize=12)
plt.xlabel('Month', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('visualizations/vibrant_theme.png', dpi=300, bbox_inches='tight')

print("✅ All custom colored charts created!")
print("\n🎨 COLOR SCHEMES USED:")
print("   Custom: #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FECA57")
print("   Business: #2c3e50, #3498db, #e74c3c, #f39c12, #27ae60")
print("   Gradient: #667eea, #764ba2, #f093fb, #f5576c, #4facfe")
