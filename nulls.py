import pandas as pd

dfNull = pd.read_csv(r"C:\Users\pedro.rrocha\Downloads\funcionarios - Null.csv")

dfNullRemovido = dfNull.dropna(subset=['departamento', 'lucro']) #remove as linhas com valores nulos
dfNullPreenchido = dfNull.fillna("nenhum") #preenche as linhas vazias com um valor especifico
dfNullPreenchidoDepartamento = dfNull
dfNullPreenchidoDepartamento['departamento'] = dfNullPreenchido['departamento'].fillna("nenhum")
dfNullPreenchidoDepartamento['lucro'] = dfNullPreenchido['lucro'].fillna(0)

dfNullPreenchido = dfNullPreenchido.fillna({'departamento': "nenhum", 'lucro':0})



print(dfNullPreenchido)
print("\n")
print(dfNullPreenchidoDepartamento)