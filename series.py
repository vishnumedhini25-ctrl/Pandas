import pandas as pd

Age = [25, 30, 35, 40, 45]
series = pd.Series(Age)
print(series)

print(series.loc[2]) 

age = [25, 30, 35, 40, 45]
series=pd.Series(age,index=["a","b","c","d","e"])

print(series.loc["d"])

print(series.iloc[1])

age={
    "Ram": 25,
    "Shyam": 30,
    "Hari": 35,
    "Rhaul": 40
}
series=pd.Series(age)
print(series)
# filtering the series
print(series[series > 30])
print(series[series < 30])