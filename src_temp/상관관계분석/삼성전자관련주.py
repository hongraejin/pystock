import pandas as pd
import os
import glob
from matplotlib import rc
rc('font',family ='Malgun Gothic')

# 잘못 다운된 데이터 제외하는 함수
def get_target_files(files):
    result = []
    for file in files:
        size = os.path.getsize(file)
        if 240000 <= size < 400000:
            result.append(file)
    return result

def get_target_df_list_2020(target_files):
    result_df_list = []
    for file in target_files:
        basename = os.path.basename(file)
        datestr = basename[:-4]
        # files 이름중 2020년도 데이터 추출 ex) basename = 20200129.csv → datestr = 2020
        if datestr.startswith("2020"):
            try:
                df = pd.read_csv(file)
                df['날짜'] = datestr
                result_df_list.append(df)
            except Exception as e:
                print(e)
                print("file read Error 발생 →  ", basename)
    return result_df_list


if __name__ == '__main__':
    # 1. 데이터 경로 설정 / 설정 필요
    DATA_DIRECTORY = "D:\\krx\\stock"
    # 2. 다운받은 데이터중 csv 파일 추출
    files = glob.glob(os.path.join(DATA_DIRECTORY, "*.csv"))
    # 3. 정상적으로 다운로드된 파일 추출
    target_files = get_target_files(files)
    # 4. 2020년도 데이터추출
    df_list_2020 = get_target_df_list_2020(target_files)
    # 5. 병합 후 pivot
    merge = pd.concat(df_list_2020, axis=0)
    # 6. 데이터 형식 정리 (문자열 -> 숫자)
    string_columns = ['현재가', '대비', '시가', '고가', '저가', '거래량', '거래대금', '시가총액', '상장주식수']
    for col in string_columns:
        merge[col] = merge[col].str.replace(",", "").astype(float)
    # 7. 상관관계 분석을 위한 pivot
    pivot_merge = merge.pivot_table(index='날짜', columns='종목명', values='시가')
    corr_matrix = pivot_merge.corr()
    result = corr_matrix['삼성전자'].sort_values(ascending=False)[:30]
    print(result)