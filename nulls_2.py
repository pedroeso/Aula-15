import pandas as pd

dfNull = pd.read_csv(r"C:\Users\pedro.rrocha\Downloads\funcionarios - Null.csv")

dfNullPreenchido = dfNull

dfNullPreenchido = dfNullPreenchido.fillna({'departamento': "nenhum", 'lucro':0})

print(dfNullPreenchido)

