import pandas as pd
print('Starting ETL...')
df = pd.read_excel('Nigerian E-Commerce Dataset.xlsx')
print('Data loaded!')
print('Shape:', df.shape)
print('Total Revenue:', df['Total Price'].sum())
