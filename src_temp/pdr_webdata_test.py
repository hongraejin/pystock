import pandas_datareader.data as web

start = '2020-01-10'
end = '2020-11-26'
# 구글 주식의 Ticker 는 "GOOG"
df = web.DataReader('GOOG','yahoo',start, end)
print(df)