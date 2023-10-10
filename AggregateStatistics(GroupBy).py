import pandas as pd

df = pd.read_csv('vgsales.csv')
print(df.head(4))
df.groupby(['Platform']).count()
print(df.head(4))