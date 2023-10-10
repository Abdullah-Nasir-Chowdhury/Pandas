import pandas as pd

df = pd.read_csv('vgsales.csv')
df.to_csv('modified.csv')
# if you wish to not save index:
df.to_csv('modified_withoutindex.csv', index=False)
# if you wish to save it to your excel:
df.to_excel('modified.xlsx', index=False)
# if you wish to save it as a .txt:
df.to_csv('modified.txt', index=False, sep='\t')
