import pandas as pd

df = pd.read_csv('vgsales.csv')
print(df.head())

# create new column:
df['Total Sales'] = df['JP_Sales'] + df['Other_Sales'] + df['Global_Sales']
print(df.head())

#drop columns:
df = df.drop(columns=['Total Sales'])
print(df.head(4))

# creating columns by iloc:
df['Total'] = df.iloc[:, 8:11].sum(axis=1)
print(df.head(4))

# get the columns as a list:
cols = list(df.columns.values)
print(cols)

# change column positions:
df = df[cols[0:7] + [cols[-1]] + cols[7:11]]
print(df)