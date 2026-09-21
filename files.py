import pandas as pd

data = pd.read_csv("customers-100.csv")
print(data)
print(data.head())
print(data.tail())
print(data.to_string())