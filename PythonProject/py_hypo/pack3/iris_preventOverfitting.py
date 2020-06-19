'''========================================================
분류모델에서 과적합 방지를위한 조치
학습/평가 데이터로 분리 후 모델 작성
k-fold를 이용해 모델 학습시 검증 작업 함께 실시
PCA를 위한 자원 축소축소

========================================================'''
from sklearn.datasets import load_iris
from sklearn.metrics._classification import accuracy_score
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
# print(iris.keys())

train_data = iris.data
train_label = iris.target
# print(train_data[:2])
# print(train_label[:2])

# 분류모델 
dt_clf = DecisionTreeClassifier()  # 다른 분류 모델 적용 가능
# print(dt_clf)
dt_clf.fit(train_data, train_label)
pred = dt_clf.predict(train_data)

print("예측값:", pred[:5])
print("실제값:", train_label[:5])
print('분류 정확도:', accuracy_score(train_label, pred))
print("과적합 발생!!")
# 정확도 100%면 매우 찝찝함. 과적합이 발생했을 가능성 농후
# 진짜 시험문제와 모의 시험문제가 같은것이나 마찬가지다.
# 과적합 방지 방안이 필요함.

print('\n----------------과적합 방지1--------------------\n')
from sklearn.model_selection import train_test_split
# 데이터 쪼개기
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=123)
dt_clf.fit(x_train, y_train)
pred2 = dt_clf.predict(x_test)
print('예측값:', pred2[:5])
print('실제값:', train_label[:5])
print('분류 정확도:', accuracy_score(y_test, pred2))

# 위의 방법도 과적합이 발생할 수 있다. 한번더 방지차원에서 k겹 교차검증을 이용가능
print("\n----------------과적합 방지2--------------------\n")

# K겹 교차 검증은 진짜 시험문제를 풀기 전, 모의 시험문제를 여러번 풀어보는 것과 비슷하다.
# train data 학습시 편중을 방지하기 위해 train data를 k번 만큼 쪼개서 학습 모델을 생성

from sklearn.model_selection import KFold
import numpy as np

feature = iris.data
label = iris.target
dt_clf = DecisionTreeClassifier(random_state=123)

kfold = KFold(n_splits=5)
print(kfold)

# 교차검증때 마다 정확도를 넣을 리스트
cv_acc = []

# print('iris shape:', feature.shape) # (150,4)
# 전체 행 수가 150. 학습데이터 : 4/5(120). 검증데이터 1/5(30). 
# 분할해서 모델을 학습한다.

n_iter = 0

for train_index, test_index in kfold.split(feature):
#     print(train_index, test_index)
    xtrain, xtest = feature[train_index], feature[test_index]
    ytrain, ytest = label[train_index], label[test_index] 
    
    # 학습 및 예측
    dt_clf.fit(xtrain, ytrain)
    pred = dt_clf.predict(xtest)
    n_iter += 1
    
    # 반복할 때 마다 정확도 측정
    acc = np.round(accuracy_score(ytest, pred), 3)
    train_size = xtrain.shape[0]
    test_size = xtest.shape[0]
    print('반복수 : {0}, 교차검증 정확도 : {1}, 학습데이터 크기: {2}, 검증데이터 크기 : {3}'.\
          format(n_iter, acc, train_size, test_size))
    cv_acc.append(acc)
    
print('평균 검증 정확도: ', np.mean(cv_acc))

print('\n--------------과적합 방지 2 추가 설명 -------------------------')
print(': 불균형한 분포도를 가진 Label 집합을 위한 k-fold 교차검증\n')
# 불균형한 분포도 : 특정 레이블 값이 특이하게 많거나 적어서 분포가 왜곡된 분포도(데이터집합)
# 방지2의 코드를 복붙하여 약간 수정

# from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold  # Stratified K-Fold
import numpy as np

feature = iris.data
label = iris.target
dt_clf = DecisionTreeClassifier(random_state=123)

skfold = StratifiedKFold(n_splits=5)
print(skfold)

# 교차검증때 마다 정확도를 넣을 리스트
cv_acc = []

# print('iris shape:', feature.shape) # (150,4)
# 전체 행 수가 150. 학습데이터 : 4/5(120). 검증데이터 1/5(30). 
# 분할해서 모델을 학습한다.

n_iter = 0

# StratifiedKFold는 split(feature, label) 해준다
for train_index, test_index in skfold.split(feature, label):  # lable을 인자로 넣어주는게 특징
#     print(train_index, test_index)
    xtrain, xtest = feature[train_index], feature[test_index]
    ytrain, ytest = label[train_index], label[test_index] 
    
    # 학습 및 예측
    dt_clf.fit(xtrain, ytrain)
    pred = dt_clf.predict(xtest)
    n_iter += 1
    
    # 반복할 때 마다 정확도 측정
    acc = np.round(accuracy_score(ytest, pred), 3)
    train_size = xtrain.shape[0]
    test_size = xtest.shape[0]
    print('반복수 : {0}, 교차검증 정확도 : {1}, 학습데이터 크기: {2}, 검증데이터 크기 : {3}'.\
          format(n_iter, acc, train_size, test_size))
    cv_acc.append(acc)
    
print('평균 검증 정확도: ', np.mean(cv_acc))  

print('\n--------------과적합 방지 2 추가 설명 -------------------------')
print(': 교차검증을 지원하는 함수를 사용\n')
from sklearn.model_selection import cross_val_score
data = iris.data
label = iris.target

# 교차 검증별 정확도 함수
score = cross_val_score(dt_clf, data, label, scoring='accuracy', cv=5)
print('교차 검증별 정확도:', np.round(score, 3))
print('평균 검증별 정확도:', np.round(np.mean(score), 3))

print('\n-------------과적합 방지 3----------------------------------')
print(':모델 생성 시 최적의 속성값(hyper parameter)을 찾아 모델 생성')
from sklearn.model_selection import GridSearchCV

# dict type으로 parameters 후보 값들을 준비
parameters = {'max_depth':[1, 2, 3], 'min_samples_split':[2, 3]}

grid_dtree = GridSearchCV(dt_clf, param_grid=parameters, cv=5, refit=True)
grid_dtree.fit(x_train, y_train)  # 내부적으로 복수개의 내부 모형 생성. 이를 모두 실행시켜 최적의 속성값을 찾음

import pandas as pd
score_df = pd.DataFrame(grid_dtree.cv_results_)
print(score_df)  # rank_test_score가 1인 경우가 최적의 속성값(hyper parameter)이다.

print('hyper parameter:', grid_dtree.best_params_)
print('최고 정확도 :', grid_dtree.best_score_)

hyper_dt_clf = grid_dtree.best_estimator_
# print(hyper_dt_clf)
hyper_pred = hyper_dt_clf.predict(x_test)
# print(hyper_pred)
print('hyper_dt_clf 정확도 : ', accuracy_score(y_test, hyper_pred))