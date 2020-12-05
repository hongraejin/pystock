import pandas as pd
import os

DATA_FOLDER = "D:\\pystock\\data\\KRX"
file_names = ['20201125.csv', '20201126.csv']
files_path = [os.path.join(DATA_FOLDER,file_name) for file_name in file_names ]

df_list = []
for file_path in files_path:
    df = pd.read_csv(file_path)
    df_list.append(df)

merged = pd.concat(df_list,axis=0)
TO_FOLDER = "D:\\pystock\\data\\Provided"
to_path = os.path.join(TO_FOLDER,'merged.xlsx')
merged.to_excel(to_path)
