import pandas as pd

df = pd.read_csv('vgsales.csv')
print(df.head(5))

# filter it:
df.loc[df['Platform']=='NES']
# assign variable to it:
df_filt=df.loc[df['Platform']=='NES']
print(df_filt)
# filter more:
df_filt=df.loc[(df['Platform']=='NES') & (df['Genre']=='Sports') & (df['Global_Sales']>3)]
print(df_filt)
# save this filtered dataframe:
df_filt.to_csv('Filtered.csv')
# reset index in filtered dataframe:
df_filt = df_filt.reset_index()
print(df_filt)
# remove old index:
df_filt = df_filt.reset_index(drop=True)
print(df_filt)
# if you don't want to save it to a new variable:
df_filt.reset_index(drop=True,inplace=True)
print(df_filt)
df_filt.drop(columns='index',inplace=True)
print(df_filt)
