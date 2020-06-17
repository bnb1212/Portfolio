'''=====================================
SVM을 활용한 iris dataset으로 품종 분류 - 3가지(다항)
====================================='''

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
# SVM 분류모델 사용
from sklearn import svm
ml = svm.SVC(C = 0.1)
print(ml)

result = ml.fit(x_train, y_train)  # train data로 모델 학습
# print(result)

# 모델 학습 후 객체를 저장
import pickle
fileName = 'final_model.sav'
pickle.dump(ml, open(fileName, 'wb'))
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

# 시각화 ------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import font_manager, rc

plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False


def plot_decision_region(X, y, classifier, test_idx=None, resolution=0.02, title=''):
    markers = ('s', 'x', 'o', '^', 'v')  # 점표시 모양 5개 정의
    colors = ('r', 'b', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    # print('cmap : ', cmap.colors[0], cmap.colors[1], cmap.colors[2])
    
    # decision surface 그리기
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    xx, yy = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))

    # xx, yy를 ravel()를 이용해 1차원 배열로 만든 후 전치행렬로 변환하여 퍼셉트론 분류기의 
    # predict()의 안자로 입력하여 계산된 예측값을 Z로 둔다.
    Z = classifier.predict(np.array([xx.ravel(), yy.ravel()]).T)
    Z = Z.reshape(xx.shape)  # Z를 reshape()을 이용해 원래 배열 모양으로 복원한다.

    # X를 xx, yy가 축인 그래프상에 cmap을 이용해 등고선을 그림

    plt.contourf(xx, yy, Z, alpha=0.5, cmap=cmap)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    X_test = X[test_idx, :]
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], c=cmap(idx), marker=markers[idx], label=cl)
    if test_idx:
        X_test = X[test_idx, :]
        plt.scatter(X_test[:, 0], X_test[:, 1], c='', linewidth=1, marker='o', s=80, label='testset')
    plt.xlabel('표준화된 꽃잎 길이')
    plt.ylabel('표준화된 꽃잎 너비')
    plt.legend(loc=2)
    plt.title(title)
    plt.show()


x_combined_std = np.vstack((x_train, x_test))
y_combined = np.hstack((y_train, y_test))
plot_decision_region(X=x_combined_std, y=y_combined, classifier=ml,

                    test_idx=range(105, 150), title='scikit-learn제공')


# 새로운 값으로 예측
new_data = np.array([[5.1, 2.4], [0.3, 0.3], [1.4, 3.4]])
new_pred = ml.predict(new_data)
print('예측 결과 :', new_pred)