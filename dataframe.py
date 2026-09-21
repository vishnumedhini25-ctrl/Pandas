import pandas as pd

students={
    "Name":["Ram","Shyam","Hari","Rhaul"],
    "Age":[25,30,35,40],
    "Department":["IT","CS","EC","MEc"]
}
df=pd.DataFrame(students,index=["std 1","std 2","std 3","std 4"])
print(df)

print(df.loc["std 2"])
print(df.iloc[2])

# adding a new column to the dataframe
df["CGPA"] = [8.5, 7.8, 9.2, 8.9]
print(df)

# adding a new row to the dataframe
new_student=pd.DataFrame({"Name":"sita","Age":28,"Department":"IT","CGPA":8.7},index=["std 5"])
df=pd.concat([df,new_student])
print(df)

# adding multiple rows to the dataframe
new_students=pd.DataFrame([
    {"Name":"gita","Age":26,"Department":"CS","CGPA":8.1},
    {"Name":"laxmi","Age":29,"Department":"EC","CGPA":8.4},
    {"Name":"Geeta","Age":25,"Department":"AI&DS","CGPA":8.2}
],index=["std 6","std 7","std 8"])
df=pd.concat([df,new_students])
print(df)
