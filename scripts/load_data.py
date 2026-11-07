import pandas as pd

df = pd.read_csv('data/orders.csv')

# print("first 5 rows of the dataset:")
# print(df.head())

# print("print the column names of the dataset:")
# print(df.columns)
#['order_id', 'order_date', 'customer', 'product', 'quantity','unit_price']

print("Before removing the duplicate rows:", len(df))

df = df.drop_duplicates()

print("After removing the duplicate rows:", len(df))

print ("Missing rows in quantity column:")
print(df[df['quantity'].isnull()])

invalid_orders = df[df['quantity'].isnull()].copy()

df = df.dropna(subset=['quantity']).copy()

print("invalid orders:", len(invalid_orders))
print("valid orders:", len(df))

# df.to_csv('data/clean_orders.csv', index= False)

# invalid_orders.to_csv("data/rejected_orders.csv", index=False)

print("cleaned and rejected orders are saved")