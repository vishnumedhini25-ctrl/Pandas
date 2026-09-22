import pandas as pd

df = pd.read_csv("Iris.csv")

df.to_json("iris.json", orient="records", indent=4)

print("JSON file created successfully!")

df = pd.read_json("iris.json")

print(df)

filtered =df[df["sepal.length"]> 5.0]
print(filtered)

filtered =df[df["petal.length"] <= 5.0]
print(filtered)

filtered =df[df["variety"] == "Setosa"]
print(filtered)

filtered =df[(df["variety"] == "Setosa") &
             (df["petal.length"] <= 5.0)]
print(filtered)