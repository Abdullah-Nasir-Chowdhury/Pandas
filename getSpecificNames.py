import pandas as pd

df = pd.read_csv('vgsales.csv')
print(df.head(4))

# use contains function
getName_Portion = df.loc[df['Name'].str.contains('Wii')]
removeName_Portion = df.loc[~df['Name'].str.contains('Wii')]
print(f'new dataframe: \n{removeName_Portion}')