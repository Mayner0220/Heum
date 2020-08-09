from konlpy.tag import Okt
from gensim.models.word2vec import Word2Vec
from data_preprocessing import training_data
import pandas as pd

okt = Okt()
tokenozed_data = []

for sentence in training_data["term"]:
    temp_X = okt.morphs(sentence, stem=True)
    tokenozed_data.append(temp_X)