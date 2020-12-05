import pandas_datareader.data as web

ticker = "PBFX"

start = "2017-01-01"
end = '2020-11-26'
df = web.DataReader(ticker, 'yahoo', start, end)
print(df.head())
df.to_excel("PBFX.xlsx",index=True)