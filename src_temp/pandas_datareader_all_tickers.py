import pandas as pd
import pandas_datareader.data as web


df = pd.read_excel("D:\\pystock\\data\\미국종목데이터.xlsx")
tickers = df['Ticker'].to_list()
print(tickers)

ticker_10 = tickers[:10]
start = '2020-01-01'
end = '2020-11-26'

df_list = []
for ticker in ticker_10:
    df = web.DataReader(ticker,'yahoo',start,end)
    df['Ticker'] = ticker
    df_list.append(df)

result = pd.concat(df_list, axis=0)
result.to_csv("D:\\pystock\\data\\USA_merged10.csv")


