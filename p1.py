
import pandas as pd
data = pd.read_csv("C:/Users\SPTINT-23/Desktop/dataset/pubg-weapon-stats.csv")
print(data)
print(data.head(5))
print(data.tail(10))
print(data.info())
print(data.dtypes)
print(data.count())
print(data["Weapon Name"])
