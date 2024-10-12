import pandas as pd

df = pd.read_csv('tornados.csv')

df_grouped = df.groupby('st')['fat'].sum().reset_index()

df_grouped.columns = ['estado', 'núm de fallecidos']

df_grouped.to_csv('fallecidos_por_estado.csv', index=False)