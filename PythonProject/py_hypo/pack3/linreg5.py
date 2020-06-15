'''=============================================
mtcars dataset으로 선형회귀분석
============================================='''

import statsmodels.api
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 폰트
plt.rc('font', family='malgun gothic')

# 데이터셋 읽기
mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars[:5])
# print(mtcars.describe())
print(mtcars.info())

# 전체 상관관계 분석
# print(mtcars.corr())

# 마력수(hp), 연비(mpg) 상관관계
print(np.corrcoef(mtcars.hp, mtcars.mpg))  # -0.7761 : 강한 음의 상관관계

# 시각화
# 산포도
plt.scatter(mtcars.hp, mtcars.mpg)
plt.xlabel('마력수')
plt.ylabel('연비')
# plt.show()
# plt.close()

# 기울기, 절편으로 예측선 긋기
slope, intercept = np.polyfit(mtcars.hp, mtcars.mpg, 1)  # R의 abline과 같은 효과
print(mtcars.hp * slope + intercept)  # wx + b
plt.plot(mtcars.hp, mtcars.hp * slope + intercept, 'pink')
plt.show()

# 단순 선형 회귀 분석
print('\n--- 단순 선형 회귀 분석 -------')
# ols model을 fit으로 학습시킨다
result = smf.ols(formula='mpg ~ hp', data=mtcars).fit()

# alpha는 신뢰구간 설정 옵션
print(result.conf_int(alpha=0.05))  # 95% 
print(result.conf_int(alpha=0.01))  # 99%

print(result.summary())
# yhat = -0.0682 * x + 30.0989
hp = 110
print('마력수가 110일 때 예측 연비:', -0.0682 * hp + 30.0989)
hp = 50
print('마력수가 50일 때 예측 연비:', -0.0682 * hp + 30.0989)
hp = 200
print('마력수가 200일 때 예측 연비:', -0.0682 * hp + 30.0989)
# msg(연비)는 hp(마력수) 값에 -0.0682배 씩 영향을 받고 있다.
# 마력에 따라 연비는 증감한다. 라고 말할 수 있으나 이는 조심스럽다. 일반적으로 독립변수는 복수이다.
# 모델이 제공한 값을 믿고 섣불리 판단하는 것은 곤란하다. 의사 결정을 위한 참고자료로 사용해야 한다.

# 다중 선형회귀 분석
print('\n--- 다중 선형회귀 분석 (독립변수가 복수) ----------------')
# 종속변수 mpg가 독립변수 hp와 wt(차체 무게)에 영향을 받는지 분석
result2 = smf.ols(formula='mpg ~ hp + wt', data=mtcars).fit()
print(result2.summary())


# 추정치 구하기
print('\n--- 추정치 구하기 : 임의의 차체 무게에 대한 연비 출력 ----------------')
print(np.corrcoef(mtcars.wt, mtcars.mpg))
result3 = smf.ols(formula='mpg ~ wt', data=mtcars).fit()
print(result3.summary()) 
# 결정계수 : 0.753
# 모델의 p-value : 모델의 p-value : 1.29e-10

# 추정치(예측값) 출력
pred = result3.predict()
print('예측값 :', pred[:3])
print('실제값 :', mtcars.mpg[:3])

data = {
        'mpg':mtcars.mpg,
        'mpg_pred':pred,
    }
df = pd.DataFrame(data)
# 실제 연비와 추정 연비가 대체적으로 비슷한 것을 알 수 있다.
print(df[:3]) 

print()
# 이제 새로운 데이터(차체 무게)로 연비를 추정해보자
# 차체 무게가 6톤이라면 연비는?
mtcars.wt = 6
new_pred = result3.predict(pd.DataFrame(mtcars.wt))
print("차체 무게가 6톤일때 : ",new_pred[0]) 
# 결과 : 5.218

# 이제 새로운 데이터(차체 무게)로 연비를 추정해보자
# 차체 무게가 400kg이라면 연비는?
mtcars.wt = 0.4
new_pred2 = result3.predict(pd.DataFrame(mtcars.wt))
print("차체 무게가 0.4톤일때 : ",new_pred2[0])
# 결과 : 35.14

# 복수 차체 무게에대한 연비 예측(데이터프레임 넣기)
wt_new = pd.DataFrame({'wt':[6,3,1,0.4,0.3]})
pred_mpgs = result3.predict(wt_new)
print("예상 연비: ",np.round(pred_mpgs.values, 3))