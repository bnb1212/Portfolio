'''=================================================
iris dataset으로 선형회귀
================================================='''

import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')
print(iris.head(2))
# 상관계수 분석
print(iris.corr())
print()
# 단순 선형회귀 모델 작성 
# sepal_length, sepal_widh : -0.117570 약한 음의 상관계수

result = smf.ols(formula = 'sepal_length ~ sepal_width', data= iris).fit()
print('결정계수 : ', result.rsquared) 
print('p-value : ', result.pvalues) # p-value 모델 : 1.518983-301

print()

result2 = smf.ols(formula = 'sepal_length ~ petal_length', data= iris).fit()
print('결정계수 : ', result2.rsquared) 
print('p-value : ', result2.pvalues) # p-value 모델 : 1.518983e-01
print('실제값 :', iris.sepal_length[0], ',예측값', result2.predict()[0])
print()

# 새로운 데이터(petal_length)로 예측(sepal_length)
new_data = pd.DataFrame({'petal_length':[1.4, 2.4, 0.4]})
y_pred = result2.predict(new_data)

print(y_pred)

# 다중 선형회귀 모델 작성
# result3 = smf.ols(formula = 'sepal_length ~ petal_length + sepal_width + petal_width', data= iris).fit()

# 독립변수로 쓸 녀석들 빼내기
col_selected = '+'.join(iris.columns.difference(['sepal_lenth', 'species']))
print(col_selected)

# 독립변수가 많을때 분리
formula = 'sepal_length ~' + col_selected
result3 = smf.ols(formula = formula, data=iris).fit()
print(result3.summary())
# 독립변수를 어떤 것을 쓰느냐가 매우 중요하다. 필요없는 변수들을 잘 제끼는 것이 필요함.

