import pandas as pd

dfNull = pd.read_csv(r"C:\Users\pedro.rrocha\Downloads\funcionarios - Null.csv")

print(dfNull.info())

dfNull['data de nascimento'] = pd.to_datetime(dfNull['data de nascimento'])

print(dfNull.info())

print(dfNull)

