from konlpy.tag import Okt
from gensim.models.word2vec import Word2Vec
from data_preprocessing import term_data

# KoNLPy를 사용하기 위해서는 JAVA_HOME 세팅과 Jpype 설정이 필수적
# 자세한 내용은 구글링을 통해 찾아볼 수 있음
# 추가) JAVA_HOME 세팅 후 컴퓨터를 껐다가 켜야 정상적으로 작동하는 것을 볼 수 있음
okt = Okt()
tokenozed_data = []
# 정규 표현식을 통한 한글 외 문자 제거 진행
term_data['term'] = term_data['term'].replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
# term_data['term'] = term_data['term'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")

for sentence in term_data["term"]:
    temp_X = okt.morphs(sentence)
    tokenozed_data.append(temp_X)

print(tokenozed_data)
# model = Word2Vec(sentence=tokenozed_data, size=100, window=5, min_count=5,
#                  workers=4, sg=0)