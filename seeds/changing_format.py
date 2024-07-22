import pandas as pd

df = pd.read_csv('raw_discounts.csv')
print(df.head())

df['discount_percentage'] = df['discount_percentage'].str.replace('%', '').astype(float)
df.to_csv('raw_discounts.csv', index=False)
