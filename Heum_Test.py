# 정규표현식을 위한 re 라이브러리 import
import re
from model_load import load_model

# Word2Vec 모델 load
Model = load_model()
Hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')

# 유사어 확인을 진행할 값을 input()을 통해 입력 받을 수 있도록 변경
Input_V = input("[Input]\n>> ")

# 보여줄 단어의 갯수를 정할 수 있도록 변경
while True:
    Show = int(input("\n[Show]\n>> "))

    if Show > 10:
        print("Error: input value error")
        continue
    elif Show < 0:
        print("Error: input value error")
        continue
    else:
        break

# return type: list
Checks = Model.wv.most_similar(Input_V)

# .wv.most_similar과 .most_similar의 차이점은 존재하지 않는 것으로 보임
# Checks = Model.most_similar("확인")

print("\n========================[Result]========================")
for check in Checks[:Show]:
    result = Hangul.sub('', str(check))
    print(result)