import pandas as pd

data_path = "D:\\pystock\\data\\Provided\\tickers_data.xlsx"
tickers_data = pd.read_excel(data_path)

to_excel_path = "D:\\pystock\\data\\Provided\\tickers_data_ver2.xlsx"
tickers_data.to_excel(to_excel_path)