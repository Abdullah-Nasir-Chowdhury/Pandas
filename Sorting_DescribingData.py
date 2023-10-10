import pandas as pd

df_csv = pd.read_csv('vgsales.csv')
print(df_csv.head(4))
print(df_csv.sort_values('Name', ascending=False))
print(df_csv.sort_values(['Name', 'Global_Sales'], ascending=False))