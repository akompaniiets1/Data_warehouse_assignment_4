import pandas as pd

df_amazon = pd.read_csv('../sources/amazon.csv')

products_df = df_amazon[['product_id', 'product_name', 'category', 'actual_price', 'img_link', 'product_link']]
discounts_df = df_amazon[['product_id', 'discounted_price', 'discount_percentage']]
reviews_df = df_amazon[['review_id', 'product_id', 'user_id', 'review_title', 'review_content']]
users_df = df_amazon[['user_id', 'user_name']].drop_duplicates()
ratings_df = df_amazon[['product_id', 'rating', 'rating_count']]

products_df.to_csv('raw_products.csv', index=False)
discounts_df.to_csv('raw_discounts.csv', index=False)
reviews_df.to_csv('raw_reviews.csv', index=False)
users_df.to_csv('raw_users.csv', index=False)
ratings_df.to_csv('raw_ratings.csv', index=False)
