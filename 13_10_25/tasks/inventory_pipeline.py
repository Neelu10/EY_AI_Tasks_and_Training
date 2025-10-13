import pandas as pd
from datetime import datetime
def run_pipeline():
    df=pd.read_csv("inventory.csv")
    df['Quantity']=df['Quantity'].astype(int)
    df['ReorderLevel'] = df['ReorderLevel'].astype(int)
    df['PricePerUnit'] = df['PricePerUnit'].astype(int)
    df['Restock Needed'] = df.apply(lambda row: 'yes' if row['Quantity'] < row['ReorderLevel'] else 'no', axis=1)
    df['Total Value'] = df['Quantity'] * df['PricePerUnit']
    df.to_csv("restock_report.csv", index = False)
    print(f" Inventory pipeline completed at {datetime.now()}")
if __name__ == "__main__":
    run_pipeline()