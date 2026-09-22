import pandas as pd
df = pd.read_json("Iris.json")
print(df)

print(df.mean(numeric_only=True))

print(df.max(numeric_only=True))

print(df.min(numeric_only=True))

print(df.sum(numeric_only=True))

print(df.count())

print(df["petal.width"].mean())