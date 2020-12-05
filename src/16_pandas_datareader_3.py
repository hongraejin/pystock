import pandas_datareader.data as web
import pandas as pd

tickers_df = pd.read_csv("D:\\pystock\\data\\Provided\\tickers_data.csv")
tickers = tickers_df['Ticker'].to_list() # Ticker 열을 list로 활용

# 상위 10개 ticker 출력
for ticker in tickers[:10]:
    print(ticker)

