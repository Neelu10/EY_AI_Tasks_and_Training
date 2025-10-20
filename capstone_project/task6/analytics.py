import pandas as pd

# Sample data
data = [
    {
        "OrderID": "O001",
        "CustomerID": "C001",
        "ProductID": "P101",
        "Quantity": 2,
        "OrderDate": "2025-10-17",
        "TotalPrice": 1600,
        "OrderMonth": "October",
        "ProductName": "Laptop",
        "Category": "Electronics",
        "Price": 800,
        "Name": "Neha",
        "Country": "India"
    },
    {
        "OrderID": "O002",
        "CustomerID": "C002",
        "ProductID": "P102",
        "Quantity": 5,
        "OrderDate": "2025-10-17",
        "TotalPrice": 100,
        "OrderMonth": "October",
        "ProductName": "Mouse",
        "Category": "Accessories",
        "Price": 20,
        "Name": "Ali",
        "Country": "UAE"
    },
    {
        "OrderID": "O003",
        "CustomerID": "C003",
        "ProductID": "P103",
        "Quantity": 3,
        "OrderDate": "2025-09-20",
        "TotalPrice": 105,
        "OrderMonth": "September",
        "ProductName": "Keyboard",
        "Category": "Accessories",
        "Price": 35,
        "Name": "Sophia",
        "Country": "UK"
    }
]

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("reports/processed_orders.csv", index=False)

# Revenue by Category
cat_rev = df.groupby("Category")["TotalPrice"].sum().reset_index()
cat_rev = cat_rev.sort_values("TotalPrice", ascending=False)
cat_rev.to_csv("reports/revenue_by_category.csv", index=False)

# Top Customers
top_customers = df.groupby(["CustomerID", "Name"])["TotalPrice"].sum().reset_index()
top_customers = top_customers.sort_values("TotalPrice", ascending=False)
top_customers.to_csv("reports/top_customers.csv", index=False)

# Monthly Revenue
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
monthly = df.groupby(df["OrderDate"].dt.to_period("M"))["TotalPrice"].sum().reset_index()
monthly["OrderMonth"] = monthly["OrderDate"].astype(str)
monthly[["OrderMonth", "TotalPrice"]].to_csv("reports/monthly_revenue.csv", index=False)

print("All reports generated and saved successfully.")