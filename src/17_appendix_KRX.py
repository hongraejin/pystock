import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',family ='Malgun Gothic')

DATA_FOLDER = "D:\\pystock\\data\\Provided_KRX_DATA"
files = glob.glob(os.path.join(DATA_FOLDER,'*'))

df_list = []
for file in files:
    df = pd.read_csv(file)
    # 파일 이름으로부터 날짜 추출
    base_name = os.path.basename(file) # 20201004.csv
    datestring = base_name[:-4]
    df['datetime'] = datestring  # 날짜 열 추가
    df_list.append(df)

# 데이터 병합
merged_KRX = pd.concat(df_list,axis=0)

# 데이터 클리닝 , 문자 제거
target_cols = ['시가','고가','저가','거래량','거래대금','시가총액','상장주식수']
for i,col in enumerate(target_cols):
    merged_KRX[col]  = merged_KRX[col].str.replace(",","")
    merged_KRX[col] = merged_KRX[col].astype(float)

# 날짜를 index, 열은 종목명, 값은 가격으로 pivot
pivoted = pd.pivot_table(merged_KRX, index='datetime',columns='종목명',values='고가')

# 종목을 기준으로 상관관계 계산, 셀트리온제약 관련주 추출. 상관계수 높은순으로 TOP10
corr_matrix_KRX = pivoted.corr()
print(corr_matrix_KRX['셀트리온제약'].sort_values(ascending=False)[:10])

list_of_bio = list(corr_matrix_KRX['셀트리온제약'].sort_values(ascending=False)[:10].index)
for item in list_of_bio:
    x = pivoted['셀트리온제약']
    y = pivoted[item]
    plt.plot(x,y,'o',label=item, alpha=.7)
    plt.xlabel('셀트리온제약 가격')
    plt.ylabel(item +" 가격")
    plt.savefig(item+".png")
    plt.show()
