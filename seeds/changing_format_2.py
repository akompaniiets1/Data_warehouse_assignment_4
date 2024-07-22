import pandas as pd

df = pd.read_csv('raw_ratings.csv')

df['rating_count'] = df['rating_count'].str.replace(',', '')

df['rating_count'] = df['rating_count'].fillna(0)

df['rating_count'] = df['rating_count'].astype(int)

df.to_csv('raw_ratings.csv', index=False)
