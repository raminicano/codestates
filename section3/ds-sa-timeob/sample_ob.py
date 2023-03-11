import pickle

model = None

with open('model.pkl','rb') as pikle_file:
    model = pickle.load(pikle_file)

X_test = [[4000]]
y_pred = model.predict(X_test)

print(f'{X_test[0][0]} sqft GrLivArea를 가지는 주택의 예상 가격은 ${int(y_pred)} 입니다.')