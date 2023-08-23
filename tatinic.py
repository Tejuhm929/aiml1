import pandas as pd
data=pd.read_csv("C:/Users/SPTINT-23/Desktop/teju/tested.csv")
p=pd.DataFrame(data)
print(p.isnull())
print(p.notnull())
print(p.fillna(0))
print(p.fillna(method="pad"))
print(p.fillna(method="bfill"))
print(p.dropna(how="all"))
