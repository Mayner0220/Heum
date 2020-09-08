from gensim.models import Word2Vec
from data_embedding import Tokenozed_data

# sentence parameter에서 에러 발생했었음 -> 인자값의 오타로 인하여 발생했었음 (fixed)
Model = Word2Vec(sentences=Tokenozed_data, size=100, window=5, min_count=5, workers=4, sg=0)

# 모델 저장
# 모델 저장 자동화 개발 진행 예정
Model.wv.save_word2vec_format("Heum_mark1")