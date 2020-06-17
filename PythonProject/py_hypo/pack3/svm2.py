'''====================================
선형(linear) 2차원 모델로는 그릴 수 없는 예측모델을 차원을 올려서 모델을 생성하는 느낌
SVM
===================================='''

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import svm, metrics

xor_data = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

# 선형분류로 해보자
xor_df = pd.DataFrame(xor_data)
print(xor_df)
#- 독립변수
feature = np.array(xor_df.iloc[:, 0:2])

#- 종속변수
label = np.array(xor_df.iloc[:, 2])


print(feature)
print(label)

#- 모델 생성(로지스틱모델, svm모델 비교
# model = LogisticRegression()
model =svm.SVC()
model.fit(feature, label)

pred = model.predict(feature)
print('pred:',pred) # [0 0 0 0]


#- 분류정확도(실제값, 예측값)
acc = metrics.accuracy_score(label, pred) 
print('분류 정확도:', acc)

#- 분류 report 
ac_report = metrics.classification_report(label, pred)
print(ac_report)



