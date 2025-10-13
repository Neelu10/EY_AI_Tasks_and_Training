import pandas as pd
from datetime import datetime
def run_pipeline():
    df=pd.read_csv("customers.csv")
    df['Age']=df['Age'].astype(int)
    df_filtered = df[df['Age'] >= 20]
    df['Age Group']=df['Age'].apply(lambda x:'young' if x<30 else ("adult" if x<50 else "senior"))
    df.to_csv("filtered_pipeline.csv", index = False)
    print(f"Pipeline completed {datetime.now()}")
if __name__ == "__main__":
    run_pipeline()