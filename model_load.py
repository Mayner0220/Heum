import gensim
from gensim.models import KeyedVectors

def load_model():
    Model = input("[Select Heum version]\n>> ")

    if(Model == "Ko"):
        Load_model = gensim.models.Word2Vec.load("./ko.bin")
    else:
        # 모델 로드
        # Heum 모델은 mark 단위별로 나누어서 저장
        Load_model = KeyedVectors.load_word2vec_format(Model)

    if(load_model):
        print("\n---------Loaded Successfully!---------\n")
        return load_model
    else:
        print("Error: Loading Model")