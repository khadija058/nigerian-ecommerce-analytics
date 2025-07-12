import pandas as pd
import os

# Create reports directory
os.makedirs('reports', exist_ok=True)

print("📊 Creating simple Excel file...")

# Load your data
try:
    df = pd.read_csv('data/processed/cleaned_data.csv')
    print("✅ Loaded your project data")
except:
    print("📥 Creating sample data")
    df = pd.DataFrame({
        'product': ['iPhone 13', 'HP Laptop', 'Samsung Phone'],
        'sales': [580000, 450000, 150000],
        'state': ['Enugu', 'Abuja', 'Lagos']
    })

# Create Excel file
excel_file = 'reports/Nigerian_Ecommerce_Analysis.xlsx'

# Export to Excel
df.to_excel(excel_file, index=False, sheet_name='Sales Data')

print(f"✅ Excel file created: {excel_file}")

# Check file size
file_size = os.path.getsize(excel_file) / 1024
print(f"📏 File size: {file_size:.1f} KB")
