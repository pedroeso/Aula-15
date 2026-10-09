import pandas as pd

dfNull = pd.read_csv(r"C:\Users\pedro.rrocha\Downloads\funcionarios - Null.csv")

dfTrocadoTipo = dfNull

print(dfNull.info())

dfTrocadoTipo['ativo'] = dfTrocadoTipo['ativo'].astype('str')

print(dfTrocadoTipo.info())
