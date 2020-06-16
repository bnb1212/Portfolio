# 날씨정보 자료를 이용해 날씨 예보(내일 비 유무)

import pandas as pd
from sklearn.model_selection._split import train_test_split 
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np

# 데이터 출처 : KIC 강남 캠퍼스 박영권 강사님 github
data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/weather.csv")

print(data.head(2), data.shape)  # (366,12)
data2 = pd.DataFrame()

# 필요없는 데이터 제거
data2 = data.drop(['Date', 'RainToday'], axis=1)
data2['RainTomorrow'] = data2['RainTomorrow'].map({'Yes':1, 'No':0})
print(data2.head(2), data2.shape)  # (366, 10)

# RainTomorrow : 종속변수, 나머지열 : 독립변수

# train / test dataset으로 분리 : 과적합(overfitting) 방지
# random_state : seed처럼 난수발생고정 
train, test = train_test_split(data2, test_size=0.3, random_state=42)

# 나눠진 데이터 확인
print(data2.shape)
print(train.shape)
print(test.shape)

# 분류 모델
# RainTomorrow를 제외한 나머지 칼럼
col_select = "+".join(train.columns.difference(['RainTomorrow']))
print(col_select)
# my_formula = 'RainTomorrow ~ MinTemp + MaxTemp + Rainfall ...'
my_formula = 'RainTomorrow ~ ' + col_select
print(my_formula)

# 분류를 위한 학습모델 생성
# model = smf.glm(formula=my_formula, data=train, family=sm.families.Binomial()).fit()
model = smf.logit(formula=my_formula, data=train).fit()

print(model)
print(model.summary())
# 예측값
# print(model.params)
print('예측값 \n', np.rint(model.predict(test)[:5]))
print('실제값 \n', np.rint(test['RainTomorrow'][:5]))

# 0.05보다 큰 P>|z|값을 가진 독립변수는 유의함에 있어 의심을 해봐야한다.

# 분류 정확도
conf_mat = model.pred_table()  # 참고 'GLMResults' object has no attribute 'pred_table'
print(conf_mat)
print((conf_mat[0][0] + conf_mat[1][1]) / len(train))

from sklearn.metrics import accuracy_score
pred = model.predict(test)
# accuracy_score는 인자를 실제값, 예측값 순으로 준다
print('분류 정확도\n', accuracy_score(test['RainTomorrow'], np.around(pred)))  # 0.872727.. 약 87%의 정확도 

