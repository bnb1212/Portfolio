'''===================================
[이항분포 검정 : 문제]

seaborn이 제공하는 tips datasets으로 어느 식당의 판매 기록자료를 구할 수 있다. 

하나의 행이 한 명의 손님을 나타낸다고 가정하자. 
열에는 성별(sex), 흡연유무(smoker), 점심/저녁(time) 등을 나타내는 데이터가 있다. 
이항 검정을 사용하여 아래의 문제를 해결하시오.

여자 손님 중 비흡연자가 흡연자보다 60% 이상 많다고 할 수 있는가?
저녁에 오는 여자 손님 중 비흡연자가 흡연자보다 80% 이상 많다고 할 수 있는가?
====================================='''
# 문1)
# 귀무 : 여자 손님 중 비흡연자가 흡연자보다 60% 이상 많지 않다.
# 대립 : 여자 손님 중 비흡연자가 흡연자보다 60% 이상 많다.

# 데이터 확인
import seaborn as sns
import scipy.stats as stats
import pandas as pd
 
tips = sns.load_dataset("tips")

print(tips.head())
print(tips.tail())


ctab = pd.crosstab(index=tips['smoker'], columns=tips['sex'])
print(ctab) # 여자손님중 yes : 33 / no : 54

# 여자손님은 총 54+33 = 87이고 54/87가 greater로 기존(가정 60%)보다 많은지 알수 있다. 
x = stats.binom_test([54, 33], p=0.6, alternative='greater')
print(x) # pvalue는 0.3907이므로 0.05보다 크다. 귀무가설을 채택.
# 비흡연자가 흡연자보다 60%이상 많지 않다.

# 문2)
# 귀무 : 저녁에 오는 여자 손님 중 비흡연자가 흡연자보다 80% 이상 많지 않다.
# 귀무 : 저녁에 오는 여자 손님 중 비흡연자가 흡연자보다 80% 이상 많다.
# print(len(tips[tips['time'] =='Dinner']))
ctab = pd.crosstab(index=tips['smoker'], columns=tips[tips['time'] =='Dinner']['sex'])
print(ctab)

x = stats.binom_test([29, 23], p=0.8, alternative='greater')
print(x) # 귀무가설 채택. 80% 많지는 않다.



