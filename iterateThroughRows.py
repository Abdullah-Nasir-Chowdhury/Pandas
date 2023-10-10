import pandas as pd

df_csv = pd.read_csv('vgsales.csv')
# iterate through rows:
for index, row in df_csv.iterrows():
    print(index, row)
for index, row in df_csv.iterrows():
    print(index, row['Name'])