# 정규표현식을 위한 re 라이브러리 import
import re
from model_load import load_model

# Word2Vec 모델 load
model = load_model()
hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')

# return type: list
checks = model.wv.most_similar("확인")

# .wv.most_similar과 .most_similar의 차이점은 존재하지 않는 것으로 보임
# checks = model.most_similar("확인")

for check in checks:
    result = hangul.sub('', str(check))
    print(result)