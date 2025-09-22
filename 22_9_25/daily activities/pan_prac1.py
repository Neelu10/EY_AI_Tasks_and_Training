import pandas as pd
import numpy as np
data={
    "Name":["alice","john","bob","chris"],
    "age":[21,45,66,33],
    "Course":["ai&ds","ml","cs",'entc'],
    "marks":[44,67,90,22]
}
df=pd.DataFrame(data)
# print(df)
# print(df["Name"])
# print(df[["Name","age"]])
# print(df.iloc[0])
# print(df.loc[2,"Course"])

# high_scorers=df[df["marks"]> 50]
# print(high_scorers)

df["Result"]=np.where(df["marks"]>=50,"Pass","Fail")
df.loc[df["Name"]=='alice',"marks"]=58
print(df)