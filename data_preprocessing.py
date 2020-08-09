import pandas as pd

file_root = "NIADic/NIADic_data.csv"

# 파이썬 인코딩 설정 환경이 맞지 않아, 에러가 발생하여 encoding을 따로 설정
# encoder는 UTF-8과 EUC-KR이 아니라, CP949를 적용해야 함
dataset = pd.read_csv(file_root, encoding="CP949")

# term 열을 제외한 다른 열을 삭제
term_data = dataset.drop(["category", "tag"], axis=1)

# term_data에서 영어가 포함된 데이터는 제거하기 위해 929143 행 이후의 데이터는 포함하지 않음
training_data = term_data.iloc[:929142]