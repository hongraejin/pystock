import pandas as pd

df1 = pd.read_csv("D:\\pystock\\data\\KRX\\20201125.csv")
df2 = pd.read_csv("D:\\pystock\\data\\KRX\\20201126.csv")

df_list = []
df_list.append(df1)
df_list.append(df2)

merged = pd.concat(df_list, axis=0)
merged.to_excel("D:\\pystock\\data\\Provided\\merged.xlsx")