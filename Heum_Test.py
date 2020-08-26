from model_load import load_model

model = load_model()

# return type: list
check = model.wv.most_similar("확인")

print(check)
print(type(check))