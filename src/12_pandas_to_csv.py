import pandas as pd

data_path = "D:\\pystock\\data\\Provided\\tickers_data.xlsx"
tickers_data = pd.read_excel(data_path)

to_csv_path = "D:\\pystock\\data\\Provided\\tickers_data.csv"
tickers_data.to_csv(to_csv_path)