'''========================================
ROC curve (Receiver Operating Characteristic curve) : FPR과 TPR을 각각 x,y축으로 놓은 그래프.
 ROC curve는 X,Y가 둘다 [0,1]의 범위이고, (0,0) 에서 (1,1)을 잇는 곡선이다.
- ROC 커브는 그 면적이 1에 가까울수록 (즉 왼쪽위 꼭지점에 다가갈수록) 좋은 성능이다. 
그리고 이 면적은 항상 0.5~1의 범위를 갖는다.(0.5이면 랜덤에 가까운 성능, 1이면 최고의 성능)
========================================='''

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np


# 분류 연습용 샘플 데이터 작성
# n_samples=샘플수, n_features=독립변수 갯수, 
x, y = make_classification(n_samples=16, n_features=2 , n_informative=2, n_redundant=0, random_state=0)

# print(x)
# print(y)

model = LogisticRegression().fit(x, y)
y_hat = model.predict(x)
print('y_hat :', y_hat)

f_value = model.decision_function(x)
print('f_value:', f_value)

print()
# np.vstack : vertical stack 배열을 위아래로 합치기 
df = pd.DataFrame(np.vstack([f_value, y_hat,y]).T, columns=['F', 'yhat', 'y'])
print(df)

# ROC 커브
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y, y_hat, labels=[1,0]))

recall = 7 / (7 + 1) # TP / (TP + FN) 재현율, 민감도, TPR, 참 양성비율
fallout = 1 / (1 + 7) # FP / (FP + TN) 허위 양성 비율, FPR
print('recall:', recall)
print('fallout:', fallout)
print()
from sklearn.metrics import roc_curve
fpr, tpr, threshold = roc_curve(y, model.decision_function(x)) 
print('tpr:',tpr)
print('fpr:',fpr)
#- 재현율을 높이기 위한 판단 기준
print('threshold:', threshold)

import matplotlib.pyplot as plt
plt.rc('font', family='d2coding') 

plt.plot(fpr, tpr, 'o-', label='Logistic Regression')
plt.plot([0,1], [0,1], 'k--', label='random guess')
plt.plot([fallout], [recall], 'ro', ms=10)
plt.xlabel('위양성율(fpr:fallout)')
plt.ylabel('재현율(tpr:recall')
plt.show()

