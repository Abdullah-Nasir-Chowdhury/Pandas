import pandas as pd

df = pd.read_csv("vgsales.csv")
print(df)
# load chunks:
df_chunks = pd.read_csv("vgsales.csv", chunksize=50)
print(df_chunks)