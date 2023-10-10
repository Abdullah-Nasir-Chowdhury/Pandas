import pandas as pd
import re

df = pd.read_csv('vgsales.csv')
# use contains method of .loc
df_new = df.loc[df['Name'].str.contains('Wii|Mario', regex=True)]
# use regex library:
df_new = df.loc[df['Name'].str.contains('bros', flags=re.I, regex=True)]
print(df_new)