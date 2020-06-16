# 분류 결과가 두 가지 이상인 경우 다항분류 모델을 사용 Logistic Regression

from sklearn import datasets
from sklearn.model_selection._split import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score 
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from nltk.chunk.util import accuracy

iris = datasets.load_iris() 
print(iris.keys())
# print(iris.DESCR)
# feature (독립 변수)
print('iris 데이터 확인 \n', iris.data[:5], iris.data.shape)  # (150, 4)
# label(class, 종속 변수)
print('\n', iris.target[:5], iris.target.shape)

# 일단 petal의 length와 width 두개만 써보자
x = iris.data[:, [2, 3]]  # petal.length, petal.width 
y = iris.target

print('---petal--- \n', x[:3])
print()
print('target : ', y[:3], ' ', set(y))

print()

# 참고 : 확률에 의해 꽃 종류가 결정되는 결정 간격 확인
log_reg = LogisticRegression()
print(log_reg)
x = iris['data'][:, 3:]
y = (iris['target'] == 2).astype(np.int)  # 0, 1로 target을 나눔
# print(x)
# print(y)

log_reg.fit(x, y)

# np.linspace() 평균 0 표준편차 3인 1000개의 난수 생성
x_new = np.linspace(0, 3, 1000).reshape(-1, 1)
# print(x_new)
print(x_new.shape)  # (1000, 1)

# 확률 값으로 출력 predict_proba
y_proba = log_reg.predict_proba(x_new)
print(y_proba)  # [[9.99250016e-01 7.49984089e-04] ... 

# 시각화
import matplotlib.pyplot as plt 
plt.plot(x_new, y_proba[:, 1], 'r-', label='virginica')
plt.plot(x_new, y_proba[:, 0], 'b--', label='notvirginica')
plt.legend()
# plt.show()
print(log_reg.predict([[1.5], [1.7]]))  # [0 1]
print(log_reg.predict([[2.5], [0.7]]))  # [1 0]
print(log_reg.predict_proba([[2.5], [0.7]])) 
# 대략 1.6보다 커지면 virginica 작으면 not virginica

# predict proba의 결과값
# [[0.02563061 0.97436939] 1번째가 0.97로 0.5를 넘음
# [0.98465572 0.01534428]] 0번째가 0.98로 0.5를 넘음 
# 따라서 [1 0]

# LogisticRegression()은 출력 값이 두 개 이상인 경우에 있어 확률 값이 큰 요소의 index가 출력된다.
# LogisticRegression()은 다중 클래스(label)를 지원하도록 일반화되어있다. softmax를 사용함.

x = iris.data[:, [2, 3]]  # petal.length, petal.width 
y = iris.target


print('-----------------------------------------')
# train / test 분류
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
print()
print("train / test :", x_train.shape, x_test.shape, y_train.shape, y_test.shape)

print('-----------------------------------------')
print('--스케일링--')
print('처리전')
print(x_train[:3])
# 스케일링 (데이크 크기 표준화)
# StandardScaler() 평균이 0, 표준편차가 1이되도록 변환해준다.
sc = StandardScaler()
print(sc)
sc.fit(x_train)
sc.fit(x_test)
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)
print('\n스케일링 처리 후')
print(x_train[:3])

print('---- 분류 모델 사용---------------')
# C= 모델에 패널티(L2 정규화)를 부여함(overfitting 관련) 모델 정확도를 조정
ml = LogisticRegression(C=0.1, random_state=0)
print(ml)

result = ml.fit(x_train, y_train)  # train data로 모델 학습
# print(result)

# 모델 학습 후 객체를 저장
import pickle
fileName = 'final_model.sav'
pickle.dump(ml, open(fileName,'wb'))
ml = pickle.load(open(fileName, 'rb'))
# ------------------------


# 분류 예측
y_pred = ml.predict(x_test)
print('예측값 :', y_pred)
print('실제값:', y_test)
print('분류 정확도:', accuracy_score(y_test, y_pred))

# confusion_matrix
con_mat = pd.crosstab(y_test, y_pred, rownames=['예측값'], colnames=['관측값'])
print(con_mat)
print((con_mat[0][0] + con_mat[1][1] + con_mat[2][2]) / len(y_test))
print(ml.score(x_test, y_test))

# 새로운 값으로 예측
new_data = np.array([[5.1, 2.4], [0.3, 0.3], [1.4, 3.4]])
new_pred = ml.predict(new_data)
print('예측 결과 :', new_pred)

