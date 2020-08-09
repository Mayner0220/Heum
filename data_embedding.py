from konlpy.tag import Okt
from gensim.models.word2vec import Word2Vec
from data_preprocessing import training_data

# anaconda에서 Jpype 설치 문제 발생
okt = Okt()
tokenozed_data = []

for sentence in training_data["term"]:
    temp_X = okt.morphs(sentence, stem=True)
    tokenozed_data.append(temp_X)

model = Word2Vec(sentence=tokenozed_data, size=100, window=5, min_count=5,
                 workers=4, sg=0)
print(model.wv.most_similar("심정현"))