import pandas as pd
import pandas_datareader as pdr
import pandas_datareader.data as web


df = pd.read_excel("D:\\pystock\\data\\미국종목데이터.xlsx")
tickers = df['Ticker'].to_list()
start = '2020-01-01'
end = '2020-11-26'

df_list = []
for i,ticker in enumerate(tickers):
    df = web.DataReader(ticker,'yahoo',start,end)
    df['ticker'] = ticker
    df_list.append(df)
    if i == 3:
        break


result = pd.concat(df_list)
result.to_csv("D:\\pystock\\data\\USA_merged.csv")