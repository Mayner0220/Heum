from gensim.models import KeyedVectors

# 모델 로드
# Heum 모델은 mark 단위별로 나누어서 저장
load_model = KeyedVectors.load_word2vec_format("Heum_mark1")