import pandas as pd
df = pd.read_json("iris.json")
print(df)

# df = df.drop(columns=["sepal.length","sepal.width"])
# print(df)

# df = df.dropna(subset=["sepal.width"])
# print(df)/

df = df.fillna({"sepal.width":3.0,
                "sepal.length":4.1})
print(df)

df["variety"] = df["variety"].replace({
    "Setosa":"S","Virginica":"Virg"
})
print(df)