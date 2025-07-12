import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def load_cleaned_data():
    """Load the cleaned data"""
    print("📖 Loading cleaned data...")
    
    file_path = 'data/processed/cleaned_data.csv'
    df = pd.read_csv(file_path)
    
    # Convert date back to datetime
    df['order_date'] = pd.to_datetime(df['order_date'])
    
    print(f"✅ Loaded {len(df)} records with {len(df.columns)} columns")
    return df

def business_overview(df):
    """Generate business overview metrics"""
    print("\n" + "="*60)
    print("💰 BUSINESS OVERVIEW")
    print("="*60)
    
    # Key metrics
    total_revenue = df['total_sales'].sum()
    total_orders = len(df)
    avg_order_value = df['total_sales'].mean()
    unique_customers = df['customer_id'].nunique()
    unique_products = df['product_name'].nunique()
    
    print(f"💵 Total Revenue: ₦{total_revenue:,}")
    print(f"📦 Total Orders: {total_orders:,}")
    print(f"📊 Average Order Value: ₦{avg_order_value:,.2f}")
    print(f"👥 Unique Customers: {unique_customers:,}")
    print(f"🛍️  Unique Products: {unique_products:,}")
    
    if unique_customers > 0:
        revenue_per_customer = total_revenue / unique_customers
        print(f"💎 Revenue per Customer: ₦{revenue_per_customer:,.2f}")
    
    return {
        'total_revenue': total_revenue,
        'total_orders': total_orders,
        'avg_order_value': avg_order_value,
        'unique_customers': unique_customers,
        'unique_products': unique_products
    }

def product_analysis(df):
    """Analyze product performance"""
    print("\n" + "="*60)
    print("🛍️  PRODUCT PERFORMANCE ANALYSIS")
    print("="*60)
    
    # Top products by sales
    print("🏆 TOP PRODUCTS BY SALES:")
    product_sales = df.groupby('product_name')['total_sales'].sum().sort_values(ascending=False)
    for i, (product, sales) in enumerate(product_sales.items(), 1):
        percentage = (sales / df['total_sales'].sum()) * 100
        print(f"  {i}. {product}: ₦{sales:,} ({percentage:.1f}%)")
    
    # Category analysis
    print("\n📦 CATEGORY PERFORMANCE:")
    category_sales = df.groupby('category')['total_sales'].sum().sort_values(ascending=False)
    for i, (category, sales) in enumerate(category_sales.items(), 1):
        avg_price = df[df['category'] == category]['unit_price'].mean()
        print(f"  {i}. {category}: ₦{sales:,} (Avg Price: ₦{avg_price:,.0f})")
    
    # Price category analysis
    print("\n💰 PRICE CATEGORY ANALYSIS:")
    price_cat_sales = df.groupby('price_category')['total_sales'].sum().sort_values(ascending=False)
    for category, sales in price_cat_sales.items():
        count = len(df[df['price_category'] == category])
        print(f"  {category}: ₦{sales:,} ({count} orders)")
    
    return product_sales, category_sales

def customer_analysis(df):
    """Analyze customer behavior"""
    print("\n" + "="*60)
    print("👥 CUSTOMER ANALYSIS")
    print("="*60)
    
    # Customer metrics
    customer_metrics = df.groupby('customer_id').agg({
        'total_sales': ['sum', 'count', 'mean'],
        'order_date': ['min', 'max']
    }).round(2)
    
    customer_metrics.columns = ['total_spent', 'order_count', 'avg_order_value', 'first_order', 'last_order']
    
    # Top customers
    print("🌟 TOP CUSTOMERS BY SPENDING:")
    top_customers = customer_metrics.sort_values('total_spent', ascending=False)
    for i, (customer_id, row) in enumerate(top_customers.iterrows(), 1):
        customer_name = df[df['customer_id'] == customer_id]['customer_name'].iloc[0]
        print(f"  {i}. {customer_name} ({customer_id}): ₦{row['total_spent']:,} ({int(row['order_count'])} orders)")
    
    # Customer behavior patterns
    print("\n📊 CUSTOMER BEHAVIOR PATTERNS:")
    
    # Repeat customers
    repeat_customers = customer_metrics[customer_metrics['order_count'] > 1]
    repeat_rate = (len(repeat_customers) / len(customer_metrics)) * 100
    print(f"  🔄 Repeat Customer Rate: {repeat_rate:.1f}%")
    
    # Average orders per customer
    avg_orders_per_customer = customer_metrics['order_count'].mean()
    print(f"  📈 Average Orders per Customer: {avg_orders_per_customer:.1f}")
    
    # Customer value distribution
    high_value = len(customer_metrics[customer_metrics['total_spent'] > customer_metrics['total_spent'].quantile(0.75)])
    medium_value = len(customer_metrics[(customer_metrics['total_spent'] > customer_metrics['total_spent'].quantile(0.25)) & 
                                       (customer_metrics['total_spent'] <= customer_metrics['total_spent'].quantile(0.75))])
    low_value = len(customer_metrics[customer_metrics['total_spent'] <= customer_metrics['total_spent'].quantile(0.25)])
    
    print(f"  💎 High Value Customers: {high_value}")
    print(f"  📈 Medium Value Customers: {medium_value}")
    print(f"  📉 Low Value Customers: {low_value}")
    
    return customer_metrics

def geographic_analysis(df):
    """Analyze geographic distribution"""
    print("\n" + "="*60)
    print("🌍 GEOGRAPHIC ANALYSIS")
    print("="*60)
    
    # Sales by state
    print("🏛️  SALES BY STATE:")
    state_sales = df.groupby('state')['total_sales'].sum().sort_values(ascending=False)
    state_orders = df.groupby('state').size()
    
    for i, (state, sales) in enumerate(state_sales.items(), 1):
        orders = state_orders[state]
        avg_order = sales / orders
        percentage = (sales / state_sales.sum()) * 100
        print(f"  {i}. {state}: ₦{sales:,} ({orders} orders, ₦{avg_order:,.0f} avg) - {percentage:.1f}%")
    
    # City analysis
    print("\n🏙️  SALES BY CITY:")
    city_sales = df.groupby('city')['total_sales'].sum().sort_values(ascending=False)
    for i, (city, sales) in enumerate(city_sales.items(), 1):
        percentage = (sales / city_sales.sum()) * 100
        print(f"  {i}. {city}: ₦{sales:,} ({percentage:.1f}%)")
    
    return state_sales, city_sales

def create_visualizations(df, metrics):
    """Create visualizations"""
    print("\n📊 Creating visualizations...")
    
    # Create reports directory
    os.makedirs('reports', exist_ok=True)
    
    # Set up the plotting style
    plt.style.use('default')
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Nigerian E-Commerce Sales Dashboard', fontsize=16, fontweight='bold')
    
    # 1. Sales by Category
    category_sales = df.groupby('category')['total_sales'].sum().sort_values(ascending=False)
    category_sales.plot(kind='bar', ax=axes[0,0], color='skyblue')
    axes[0,0].set_title('Sales by Category')
    axes[0,0].set_ylabel('Sales (₦)')
    axes[0,0].tick_params(axis='x', rotation=45)
    
    # 2. Sales by State
    state_sales = df.groupby('state')['total_sales'].sum().sort_values(ascending=False)
    state_sales.plot(kind='bar', ax=axes[0,1], color='lightgreen')
    axes[0,1].set_title('Sales by State')
    axes[0,1].set_ylabel('Sales (₦)')
    axes[0,1].tick_params(axis='x', rotation=45)
    
    # 3. Price Category Distribution
    price_dist = df['price_category'].value_counts()
    price_dist.plot(kind='pie', ax=axes[1,0], autopct='%1.1f%%')
    axes[1,0].set_title('Orders by Price Category')
    axes[1,0].set_ylabel('')
    
    # 4. Daily Sales Trend
    daily_sales = df.groupby('order_date')['total_sales'].sum()
    daily_sales.plot(kind='line', ax=axes[1,1], marker='o', color='orange')
    axes[1,1].set_title('Daily Sales Trend')
    axes[1,1].set_ylabel('Sales (₦)')
    axes[1,1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('reports/sales_dashboard.png', dpi=300, bbox_inches='tight')
    print("✅ Dashboard saved as 'reports/sales_dashboard.png'")
    
    # Show the plot
    plt.show()

def generate_insights_report(df, metrics):
    """Generate business insights report"""
    print("\n" + "="*60)
    print("💡 KEY BUSINESS INSIGHTS")
    print("="*60)
    
    insights = []
    
    # Revenue insights
    insights.append(f"💰 Total business revenue is ₦{metrics['total_revenue']:,}")
    insights.append(f"📊 Average order value is ₦{metrics['avg_order_value']:,.2f}")
    
    # Product insights
    top_product = df.groupby('product_name')['total_sales'].sum().idxmax()
    top_category = df.groupby('category')['total_sales'].sum().idxmax()
    insights.append(f"🏆 Best selling product: {top_product}")
    insights.append(f"📦 Top category: {top_category}")
    
    # Geographic insights
    top_state = df.groupby('state')['total_sales'].sum().idxmax()
    insights.append(f"🌍 Top performing state: {top_state}")
    
    # Customer insights
    repeat_customers = df.groupby('customer_id').size()
    repeat_rate = (repeat_customers > 1).mean() * 100
    insights.append(f"👥 Customer repeat rate: {repeat_rate:.1f}%")
    
    # Price insights
    premium_sales = df[df['price_category'] == 'Premium']['total_sales'].sum()
    premium_percentage = (premium_sales / df['total_sales'].sum()) * 100
    insights.append(f"💎 Premium products contribute {premium_percentage:.1f}% of sales")
    
    # Print insights
    for i, insight in enumerate(insights, 1):
        print(f"  {i}. {insight}")
    
    # Save insights to file
    with open('reports/business_insights.txt', 'w') as f:
        f.write("NIGERIAN E-COMMERCE BUSINESS INSIGHTS\n")
        f.write("="*50 + "\n\n")
        for insight in insights:
            f.write(f"• {insight}\n")
    
    print(f"\n✅ Insights saved to 'reports/business_insights.txt'")

def main():
    """Main analysis function"""
    print("🚀 Nigerian E-Commerce Sales Analysis")
    print("="*50)
    
    # Load data
    df = load_cleaned_data()
    
    # Run all analyses
    metrics = business_overview(df)
    product_analysis(df)
    customer_analysis(df)
    geographic_analysis(df)
    
    # Create visualizations
    create_visualizations(df, metrics)
    
    # Generate insights report
    generate_insights_report(df, metrics)
    
    print("\n🎉 Complete analytics pipeline finished!")
    print("📁 Check the 'reports' folder for:")
    print("   📊 sales_dashboard.png - Visual dashboard")
    print("   📝 business_insights.txt - Key findings")

if __name__ == "__main__":
    main()
