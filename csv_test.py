import pandas as pd

df = pd.read_csv('./exemplo.csv') # type: ignore

df_filtrado = df[df["Produto"] == "Notebook Gamer"]
print(df_filtrado)
df_filtrado = df[df['Data'] == '2023-01-15']
print(df_filtrado)



df2 = pd.read_csv('./exemplo2.csv')
df_filtrado2 = df2[(df2['Produto'] == 'Mouse Sem Fio') & (df2['Venda'] > 20)]
# df_filtrado2 = df2[df2['Venda'] > 20]
print(df_filtrado2)