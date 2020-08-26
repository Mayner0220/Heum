import gensim
from gensim.models import KeyedVectors

def load_model():
    model = input("[Select Heum version]\n>> ")

    if(model == "Ko"):
        load_model = gensim.models.Word2Vec.load("./ko.bin")
    else:
        # 모델 로드
        # Heum 모델은 mark 단위별로 나누어서 저장
        load_model = KeyedVectors.load_word2vec_format(model)

    if(load_model):
        print("Loaded Successfully!")
        return load_model
    else:
        print("Error: Loading Model")