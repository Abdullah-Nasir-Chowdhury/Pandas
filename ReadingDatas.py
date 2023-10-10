import numpy as np
import pandas as pd

df_csv = pd.read_csv("vgsales.csv")
# Read columns:
print(df_csv.columns)
# Read specific columns:
print(df_csv['Name'])
# specify the number:
print(df_csv['Name'][0:10])
# Read multiple columns:
print(df_csv[['Name','Platform','Year']][0:10])


print(df_csv.head(4))
# Read rows:
# single row:
print(df_csv.iloc[1])
# Read multiple rows:
print(df_csv.iloc[0:4])


# Read specific location (R,C):
print(df_csv.iloc[2,1])

# Read specific location:
print(df_csv.loc[df_csv['Platform']=='Wii'])



