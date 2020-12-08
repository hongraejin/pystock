import pandas as pd
import seaborn as sns
import os
import sys
import glob
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',family ='Malgun Gothic')

# 데이터 input, output 경로 지정
BASE_DIRECTORY = "D:\\국내주식"

DATA_PATH = "stock"
DATA_DIRECTORY = os.path.join(BASE_DIRECTORY, DATA_PATH)

OUTPUT_PATH = "OUTPUT"
OUTPUT_DIRECTORY = os.path.join(BASE_DIRECTORY, OUTPUT_PATH)

files = glob.glob(os.path.join(DATA_DIRECTORY,'*'))

def get_merged_df(files):
    """
    :param files, csv files:
    :return: DataFrame
    """
    df_list = []
    for file in files:
        df = pd.read_csv(file)
        date_str_with_type = os.path.basename(file)
        date_str = date_str_with_type.split('.')[0]
        df['날짜'] = date_str
        df_list.append(df)

    merged = pd.concat(df_list)
    return merged

def set_merged_df(merged):
    result = merged

    # 날짜 데이터 변환
    result['날짜'] = pd.to_datetime(merged['날짜'], format='%Y%m%d')

    # 문자열 데이터중 숫자형으로 바꾸는 것 변환
    string_columns = ['현재가', '대비', '시가', '고가', '저가', '거래량', '거래대금', '시가총액', '상장주식수']
    for col in string_columns:
        result[col] = result[col].str.replace(",", "").astype(float)

    return result

def get_related_top(merge, stock_name ,n=30):
    pivot_merge = merge.pivot_table(index='날짜', columns='종목명', values='시가')
    corr_matrix = pivot_merge.corr()
    result = corr_matrix[stock_name].sort_values(ascending=False)[:n].to_frame()
    outpath = os.path.join(OUTPUT_DIRECTORY,stock_name+"_TOP_"+str(n)+".xlsx")
    result.to_excel(outpath)
    return result


merged = get_merged_df(files)
merged = set_merged_df(merged)
finished = get_related_top(merged,'에이치엘비')

print(finished)
