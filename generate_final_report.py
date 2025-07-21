import pandas as pd
import os
from datetime import datetime

print("📋 Generating Executive Report...")

# Load data
df = pd.read_excel("data/Nigerian E-Commerce Dataset.xlsx")
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Calculate key metrics
total_revenue = df["Total Price"].sum()
total_orders = df["Order ID"].nunique()
total_items = df["Quantity"].sum()
avg_order_value = total_revenue / total_orders

# Generate report
report = f"""
NIGERIAN E-COMMERCE BUSINESS REPORT
==================================================

EXECUTIVE SUMMARY:
- Total Revenue: ₦{total_revenue:,.2f}
- Total Orders: {total_orders:,}
- Average Order Value: ₦{avg_order_value:,.2f}
- Total Items Sold: {total_items:,}

TOP 5 REGIONS:"""

top_regions = df.groupby("Order Region")["Total Price"].sum().sort_values(ascending=False).head(5)
for i, (region, revenue) in enumerate(top_regions.items(), 1):
    percentage = (revenue / total_revenue) * 100
    report += f"\n{i}. {region}: ₦{revenue:,.0f} ({percentage:.1f}%)"

report += f"""

TOP 5 PRODUCTS:"""

top_products = df.groupby("Item Name")["Quantity"].sum().sort_values(ascending=False).head(5)
for i, (product, qty) in enumerate(top_products.items(), 1):
    report += f"\n{i}. {product}: {qty:,} units"

report += """

RECOMMENDATIONS:
1. Focus on Lagos market (dominant region)
2. Expand top-selling products inventory
3. Investigate growth in other regions
4. Leverage high AOV for premium strategy
"""

# Save report
os.makedirs("reports", exist_ok=True)
with open("reports/final_business_report.txt", "w") as f:
    f.write(report)

print("✅ Final report saved!")
print(report)
