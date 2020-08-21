from model_load import load_model
import gensim

model = gensim.models.Word2Vec.load("./ko.bin")
print(model.wv.most_similar("한국"))