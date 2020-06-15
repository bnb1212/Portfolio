'''=================================================
회귀분석 문제 2) 
student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오.
  - 국어 점수를 입력하면 수학 점수 예측
  - 국어, 영어 점수를 입력하면 수학 점수 예측
================================================='''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression

# 폰트
plt.rc('font', family='d2coding')

df = pd.read_csv('../testdata/student.csv')
print(df.head(3))
print(df.corr())
print()

# 시각화
plt.scatter(df['국어'], df['수학'])
plt.xlabel('국어')
plt.ylabel('수학')
# plt.show()
# plt.close()


# 기울기, 절편으로 예측선 긋기
slope, intercept = np.polyfit(df['국어'], df['수학'], 1)  # R의 abline과 같은 효과
print(df['국어'] * slope + intercept)  # wx + b
plt.plot(df['국어'], df['국어'] * slope + intercept, 'pink')
plt.show()

# 데이터 학습 및 예측
result = smf.ols(formula='수학 ~ 국어', data=df).fit()

# print(result.summary())
# yhat = 0.5705 * kor + 32.1069
kor = 80
print('국어점수가 80일 때 예측 수학점수:', np.around(0.5705 * kor + 32.1069))

# ========= 해석 ==================================== 
# 수학점수는 국어점수값에 0.5705배 씩 영향을 받고 있다.

print('\n -------------------- 다중 회귀 분석 -------------------------')

result2 = smf.ols(formula='수학 ~ 국어 + 영어', data=df).fit()
print(result2.summary())

# yhat = 0.1158 * kor + 0.5942 * eng + 22.6238
kor = 70
eng = 45
print('국어점수가 70, 영어점수가 45일때 예측 수학 점수 :',np.around(0.1158 * kor + 0.5942 * eng + 22.6238))
print('국어점수와 영어점수는 수학점수를 결정계수 0.659, 약 66%정도 설명하는데 있어 유의하다')