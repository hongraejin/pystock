import pandas_datareader.data as web
import pandas as pd

tickers_df = pd.read_csv("D:\\pystock\\data\\Provided\\tickers_data.csv")
tickers = tickers_df['Ticker'].to_list() # Ticker 열을 list로 활용

# 상위 10개 ticker 출력
df_list = []
for ticker in tickers[:10]:
    df = web.DataReader(ticker, "yahoo",start='2020-01-01', end='2020-11-30')
    df['Ticker'] = ticker
    df_list.append(df)

merge_USA = pd.concat(df_list, axis=0)
merge_USA.to_csv("D:\\pystock\\data\\Provided\\ticker10_merged.csv")
