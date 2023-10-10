import pandas as pd

df = pd.read_csv('vgsales.csv')
print(df.head(4))
# change particular names in column:
df.loc[df['Platform']=='Wii', 'Platform'] = 'Fire!'
print(df.head(4))
