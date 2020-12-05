import pandas as pd

# df = pd.read_csv("D:\\pystock\\data\\20200129.csv")
# df.to_excel("D:\\pystock\\data\\20200129.xlsx")


# result = pd.date_range(start="2020-01-01", end="2020-11-26")
# print(result)


# result = pd.date_range(start="2020-01-01", end="2020-11-26", freq='B')
# print(result)

df1 = pd.read_csv("D:\\pystock\\data\\20200129.csv")
df2 = pd.read_csv("D:\\pystock\\data\\20200130.csv")

df_list = [df1,df2]
merge_df = pd.concat(df_list, axis=0)
merge_df.to_csv("D:\\pystock\\data\\merged2930.csv")

