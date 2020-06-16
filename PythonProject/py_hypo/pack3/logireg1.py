'''================================================
Logistic Regression : 지도학습 중 이항 분류 모델
독립변수는 연속형. 종속변수는 범주형
logit 변환( odds ratio 의 결과에 log를 씌워 0~ 1사이의 확률값을 반환한다.)
==============================================='''

# sigmoid function(시그모이드 함수)
# 1 / (1 + e ** (-x))
import math
import numpy as np
from sklearn.ensemble.tests.test_partial_dependence import sample_weight
from sklearn.metrics._scorer import accuracy_scorer
def sigmoidFunc(x):
    return 1 / (1+math.exp(-x))

# 시그모이드 함수를 지나 0~1사이의 값
print(sigmoidFunc(1))
print(sigmoidFunc(3))
print(sigmoidFunc(-2))
print(sigmoidFunc(0.2))
print(sigmoidFunc(0.8))

# np.around를 활용하여 0 또는 1의 값을 얻을 수 있다.
print(np.around(sigmoidFunc(0.2)))
print(np.around(sigmoidFunc(0.8)))
print(np.rint(sigmoidFunc(0.8))) # rint도 사용가능

print('car '*20)
import statsmodels.api as sm
import statsmodels.formula.api as smf

# 연습 : 자동차 데이터로 분류 연습 ( 연비와 마력수로 변속기 분류 )
mtcars = sm.datasets.get_rdataset('mtcars').data
print(mtcars.head(2))
mtcar = mtcars.loc[:, ['mpg', 'hp', 'am']] # am : 변속기 종류(수동, 자동)
print(mtcar.head(2))
print(mtcar['am'].unique()) # [1, 0]

# 연습 1 : logit()
formula = 'am ~ hp + mpg'
result = smf.logit(formula = formula, data = mtcar).fit()
print(result)
print(result.summary())
# 95%의 신뢰구간
# 두 독립변수의 P>|z| 가 0.05보다 작으므로 유의
pred = result.predict(mtcar[:5])
print('==예측 값== \n',np.around(pred))
print('\n==실제 값== \n', mtcar['am'][:5])

# confusion matrix
conf_tab = result.pred_table()
print(conf_tab)

# print('분류 정확도(accuracy) :', (16 + 10) / len(mtcar))
print('분류 정확도(accuracy) :', (conf_tab[0][0] + conf_tab[1][1]) /len(mtcar))
from sklearn.metrics import accuracy_score
pred2 = result.predict(mtcar)
print('분류 정확도(accuracy) :', accuracy_score(mtcar['am'], np.around(pred2))) # 0.8125

print('------------------------------------------------------------------------------')
# 연습 2 : glm()
result2 = smf.glm(formula = formula, data=mtcar, family = sm.families.Binomial()).fit()
print(result2)
print(result2.summary())

glm_pred = result2.predict(mtcar[:5])
print('glm_pred : ',glm_pred)
print('glm_pred :',np.around(glm_pred))
glm_pred2 = result2.predict(mtcar)

print('분류정확도 : ',accuracy_score(mtcar['am'], np.around(glm_pred2))) # 0.8125

# 예를 들어 강아지 사진을 컴퓨터에게 학습을 시킬때 컴퓨터는 강아지 사진들을 받아 분류를 한다.
# 그런데 꼬리가 없는 강아지 사진이 들어오면, 머신러닝은 그동안의 학습데이터로 강아지로 분류할 수 있어야한다.
# 분류정확도 100%의 결과값을 찾는 것이 아닌 주변값도 포용할 수 있는 값을 찾는 것이 목적이다.
# 100% 모델이 나온다면, 과적합이 되어있는 모델일 가능성이 있다. 
# 머신러닝은 수학이 아닌 추론이다. 

# 새로운 값으로 예측
# newdf = mtcar.iloc[:2]  
newdf = mtcar.iloc[:2].copy()  
print(newdf)
newdf['mpg'] = [10, 30]
newdf['hp'] = [100, 120]  # 기존 데이터를 일부 추출해 새 DF 객체 생성. 분류 작업
print(newdf)
new_pred = result2.predict(newdf)
print('새로운 데이터에 대한 분류결과\n',new_pred)
print('새로운 데이터에 대한 분류결과\n',np.around(new_pred))
print('새로운 데이터에 대한 분류결과\n',np.rint(new_pred))

print('---------------------')
import pandas as pd
newdf2 = pd.DataFrame({'mpg':[10,35], 'hp':[100, 125]})
print(newdf2)
new_pred2 = result2.predict(newdf2)
print('새로운 데이터에 대한 분류 결과\n', np.around(new_pred2))