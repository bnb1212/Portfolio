'''============================================
Naive Bayes Classification : 베이즈 정리를 적용한 확률 분류기
텍스트 분류에 효과적 - 스팸메일, 게시판 카테고리 등의 분류에 많이 사용됨
ML에서는 feature가 주어졌을 때 label의 확률을 구하는데 사용
P(L|feature) = P(feature)L)P(L) / P(feature)

-- 위키 --
특성들 사이의 독립을 가정하는 베이즈 정리를 적용한 확률 분류기의 일종으로 1950 년대 이후 광범위하게 연구되고 있다.

통계 및 컴퓨터 과학 문헌에서 , 나이브 베이즈는 단순 베이즈, 독립 베이즈를 포함한 다양한 이름으로 알려져 있으며,
 1960 년대 초에 텍스트 검색 커뮤니티에 다른 이름으로 소개되기도 하였다.

나이브 베이즈 분류는 텍스트 분류에 사용됨으로써 문서를 여러 범주 (예: 스팸, 스포츠, 정치)중 하나로 판단하는 문제에 대한 대중적인 방법으로 남아있다. 
또한, 자동 의료 진단 분야에서의 응용사례를 보면, 적절한 전처리를 하면 더 진보 된 방법들 (예: 서포트 벡터 머신 (Support Vector Machine))과도 
충분한 경쟁력을 보임을 알 수 있다.
============================================='''

from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder

x = np.array([1, 2, 3, 4, 5])
x = x[:, np.newaxis]
print(x)
y = np.array([1, 3, 5, 7, 9 ])

# 모델생성(가우시안 NB)
model = GaussianNB().fit(x, y)
print(model)
pred = model.predict(x)
print(pred)

# 새 값
new_x = np.array([[0.5], [3.1], [15.0]])
new_pred = model.predict(new_x)
print(new_pred)


print('----OneHotEncoding(희소 행렬의 일종)---------------------------')
x = np.array([1, 2, 3, 4, 5])
# numpy의 eye메소드로 진행
x = np.eye(x.shape[0])
print(x)

y = np.array([1, 3, 5, 7, 9 ])
model = GaussianNB().fit(x, y)
print(model)
pred = model.predict(x)
print(pred)

acc = metrics.accuracy_score(y, pred)
print('accuracy : ', acc)

# 새 값
new_x = np.array([[0.5], [7.1], [12.0]])
new_pred = model.predict(new_x)
print(new_pred)

print('----OneHotEncoding : One Hot Encoder 활용---------------------------')
x = np.array([1,2,3,4,5])
one_hot = OneHotEncoder(categories='auto')
print(one_hot) 

# 차원확장
x = x[:, np.newaxis]

x = one_hot.fit_transform(x).toarray()
print(x)