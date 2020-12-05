import pandas as pd

df1 = pd.read_csv("D:\\pystock\\data\\20200129.csv")
df2 = pd.read_csv("D:\\pystock\\data\\20200130.csv")

df_list = [df1,df2]
merge_df = pd.concat(df_list,axis=0)
merge_df.to_csv("D:\\pystock\\data\\merged29-30.csv")