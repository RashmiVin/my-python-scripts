import pandas as pd

titanic = pd.read_csv("data/titanic.csv")
print("\n\n\n=========================================================")
print("##################  Printing the first 8 rows  ##################")
print(titanic.head(8))


print("\n\n\n=========================================================")
print("##################  Printing the last 2 rows  ##################")
print(titanic.tail(2))

print("\n\n\n=========================================================")
print("##################  Printing the types  ##################")
print(titanic.dtypes)

print("\n\n\n=========================================================")
print("##################  Now converting to XLSX  ##################")
titanic.to_excel("data/titanic.xlsx", sheet_name="passengers", index=False)

print("\n\n\n=========================================================")
print("##################  Printing the info  ##################")
titanic.info()

print("\n\n\n=========================================================")
print("##################  Now printing only the ages and its shape  ##################")
ages = titanic["Age"]
print(ages)
print(ages.shape)


print("\n\n\n=========================================================")
print("##################  Now printing the age and sex and their shape  ##################")
ageAndSex = titanic[["Age", "Sex"]]
print(ageAndSex)
print(ageAndSex.shape)


print("\n\n\n=========================================================")
print("##################  Now selecting rows with age above 50  ##################")
above35 = titanic[titanic["Age"] > 50]
print(above35)
print(above35.shape)


print("\n\n\n=========================================================")
print("##################  Now selecting 1 row with Id equal to 1  ##################")
oneRow = titanic[titanic["PassengerId"] == 1]
print(oneRow)
print(oneRow.shape)


print("\n\n\n=========================================================")
