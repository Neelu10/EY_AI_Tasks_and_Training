import pandas as pd
from datetime import datetime

def run_pipeline():
    products = pd.read_csv("products.csv")
    orders = pd.read_csv("orders.csv")
    customers = pd.read_csv("customers1.csv")

    df = pd.merge(orders, customers, on="CustomerID")
    df = pd.merge(df, products, on="ProductID")

    # Fixing HTML entities
    df = df[(df['Quantity'] >= 2) & (df['Country'].isin(["India", "UAE"]))]

    df['Quantity'] = df['Quantity'].astype(int)
    df['Price'] = df['Price'].astype(int)
    df['Total Value'] = df['Quantity'] * df['Price']
    df['OrderDate'] = pd.to_datetime(df['OrderDate'])
    df["OrderMonth"] = df['OrderDate'].dt.month_name()

    # Fixing column name from TotalAmount to Total Value
    category_summary = (
        df.groupby("Category", as_index=False)["Total Value"]
        .sum()
        .rename(columns={"Total Value": "TotalRevenue"})
    )

    segment_summary = (
        df.groupby("Segment", as_index=False)["Total Value"]
        .sum()
        .rename(columns={"Total Value": "TotalRevenue"})
    )

    # Define customer_revenue
    customer_revenue = (
        df.groupby("CustomerID", as_index=False)["Total Value"]
        .sum()
        .rename(columns={"Total Value": "TotalRevenue"})
    )

    # Save to CSV
    df.to_csv("processed_orders.csv", index=False)
    category_summary.to_csv("category_summary.csv", index=False)
    segment_summary.to_csv("segment_summary.csv", index=False)
    customer_revenue.to_csv("customer_revenue.csv", index=False)

    print(f"Pipeline completed {datetime.now()}")
    print(df.head())
    print(category_summary)

if __name__ == "__main__":
    run_pipeline()



#
# import pandas as pd
# from datetime import datetime
# def run_pipeline():
#     products=pd.read_csv("products.csv")
#     orders = pd.read_csv("orders.csv")
#     customers=pd.read_csv("customers1.csv")
#
#
#     df=pd.merge(orders,customers,on="CustomerID")
#     df=pd.merge(df,products,on="ProductID")
#     df=df[(df['Quantity']>=2)&(df['Country'].isin(["India","UAE"]))]
#
#     df['Quantity'] = df['Quantity'].astype(int)
#     df['Price'] = df['Price'].astype(int)
#     df['Total Value'] = df['Quantity'] * df['Price']
#     df['OrderDate']=pd.to_datetime(df['OrderDate'])
#     df["OrderMonth"] = df['OrderDate'].dt.month_name()
#
#     category_summary = (
#         df.groupby("Category", as_index=False)["TotalAmount"]
#         .sum()
#     )
#     segment_summary=(df.groupby("Segment",as_index=False)["TotalAmount"].sum())
#
#
#     df.to_csv("processed_orders.csv", index = False),
#     category_summary.to_csv("category_summary.csv", index=False),
#     segment_summary.to_csv("segment_summary.csv", index=False),
#     customer_revenue.to_csv("customer_revenue.csv", index=False)
#     print(f"Pipeline completed {datetime.now()}")
#     print(df.head())
#     print(category_summary)
# if __name__ == "__main__":
#     run_pipeline()