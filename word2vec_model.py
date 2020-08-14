from gensim.models import Word2Vec
from data_embedding import tokenozed_data

# sentence parameter에서 에러 발생
model = Word2Vec(sentence=tokenozed_data, size=100, window=5, min_count=5,
                 workers=4, sg=0)

# 모델 저장
model.wv.save_word2vec_format("Heum_mark1")

# 모델 로드
# load_model = KeyedVectors.load_word2vec_format("Heum_mark1")

model_result = model.wv.most_similar("과자")
print(model_result)