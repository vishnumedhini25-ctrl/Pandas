import pandas as pd

df=pd.read_csv("customers-100.csv", index_col="Customer Id")
print(df["City"])
print(df["Last Name"].to_string())

print(df[["Last Name","First Name","City"]].to_string())
print(df.loc["28CDbC0dFe4b1Db"])

print(df.loc["28CDbC0dFe4b1Db",["First Name","Last Name","Phone 1"]])

print(df.loc["28CDbC0dFe4b1Db":"a940cE42e035F28",["First Name","Last Name","Phone 1"]])

print(df.iloc[0:5])

print(df.iloc[0:5,1:3])