from gensim.models import Word2Vec
from data_embedding import tokenozed_data

# sentence parameter에서 에러 발생했었음 -> 인자값의 오타로 인하여 발생했었음 (fixed)
model = Word2Vec(sentences=tokenozed_data, size=100, window=5, min_count=5, workers=4, sg=0)

# 모델 저장
model.wv.save_word2vec_format("Heum_mark1")