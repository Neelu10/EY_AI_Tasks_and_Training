import pandas as pd
# Loading the  CSV files
customer = pd.read_csv("customers.csv")
product = pd.read_csv("products.csv")
order = pd.read_csv("orders.csv")

# joining the data
df = order.merge(product, how='left', on='ProductID')
df = df.merge(customer, how='left', on='CustomerID')

# Calculating the  total price
df['TotalPrice'] = df['Quantity'].astype(float) * df['Price'].astype(float)

# Converting  OrderDate to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Extracting  month name
df["OrderMonth"] = df['OrderDate'].dt.month_name()

# Selecting  relevant columns
result = df[['OrderID', 'OrderDate', 'OrderMonth', 'CustomerID', 'Name', 'Country',
             'ProductID', 'ProductName', 'Category', 'Quantity', 'Price', 'TotalPrice']]

# Save to CSV
result.to_csv("processed_orders.csv", index=False)
print("Data saved to processed_orders.csv")