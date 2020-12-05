import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',family ='Malgun Gothic')

# data 생성시점은 W48로 현재 Volume 과 차이있음, volume이 높은 순으로 TOP 6 추출
ticker_df = pd.read_csv("D:\\pystock\\data\\Provided\\tickers_data.csv")
energy_sector = ticker_df[ticker_df['Sector']=='Energy']
volume_top6_df_index = energy_sector['Volume'].str.replace(",","").astype(float).sort_values(ascending=False)[:6].index

targets = ticker_df.loc[volume_top6_df_index]
print(targets)
targets_ticker = targets['Ticker'].to_list()

for target_ticker in targets_ticker:

    df = web.DataReader(target_ticker,'yahoo','2020-09-01','2020-11-30')
    item_trend = df['Close'] # 일별 장 마감시간 기준 가격

    plt.plot(item_trend,'o', alpha=.7)
    plt.title(target_ticker)
    plt.savefig("해외"+target_ticker+'.png')
    plt.show()



