import pandas as pd

print('Starting ETL...')

# Try different possible paths
try:
    df = pd.read_excel('Nigerian E-Commerce Dataset.xlsx')
    print('✅ Found file in current directory')
except FileNotFoundError:
    try:
        df = pd.read_excel('data/Nigerian E-Commerce Dataset.xlsx')
        print('✅ Found file in data directory')
    except FileNotFoundError:
        print('❌ File not found. Let me check what files exist...')
        import os
        print('Files in current directory:', [f for f in os.listdir('.') if f.endswith('.xlsx')])
        if os.path.exists('data'):
            print('Files in data directory:', [f for f in os.listdir('data') if f.endswith('.xlsx')])
        exit()

print('Data loaded successfully!')
print('Shape:', df.shape)
print('Total Revenue: ₦{:,.2f}'.format(df['Total Price'].sum()))
