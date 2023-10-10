# Working with pandas series data structure

import pandas as pd
import numpy as np
import openpyxl
# series: it is a single dimensional dataframe
# dataframe: multi dimensional


# Loading datas into Pandas:
# read csv file:
df_csv = pd.read_csv("vgsales.csv")
print(df_csv)
print(df_csv.head(10))
print(df_csv.tail(5))

# # read excel file:
# df_xlsx = pd.read_excel("vgsales.xlsx")
# print(df_xlsx)
# print(df_xlsx.head(3))
# print(df_xlsx.tail(3))
#
# # read .txt file:
# df_txt = pd.read_csv("vgsales.txt", delimeter='\t')
# # the delimeter attribute adds tabs or spaces between texts
# print(df_txt)
# print(df_txt.head())
# print(df_txt.tail())

