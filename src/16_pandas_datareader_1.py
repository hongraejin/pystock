import pandas_datareader.data as web

start = "2020-01-01"
end = "2020-11-26"

# 구글의 Ticker 는 "GOOG"
ticker = "GOOG"
df = web.DataReader(ticker, "yahoo", start, end)
print(df)