import pandas as pd

file_root = "NIADic/NIADic_data.csv"

# 파이썬 인코딩 설정 환경이 맞지 않아, 에러가 발생하여 encoding을 따로 설정
# encoder는 UTF-8과 EUC-KR이 아니라, CP949를 적용해야 함
Dataset = pd.read_csv(file_root, encoding="CP949")

# term 열을 제외한 다른 열을 삭제
Term_data = Dataset.drop(["category", "tag"], axis=1)