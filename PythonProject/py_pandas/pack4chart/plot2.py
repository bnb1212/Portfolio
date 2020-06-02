# 시각화
import numpy as np
import matplotlib.pyplot as plt

# 한글깨짐 방지
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False

# # figure 선언하고 subplot 추가하기
# 
# # 차트 영역에 대한 객체 선언 
# fig = plt.figure()
# 
# # 서브 플롯 추가
# ax1 =  fig.add_subplot(1, 2, 1)
# ax2 =  fig.add_subplot(1, 2, 2)
# 
# # hist() : 히스토그램 / bins : 구간 수 / alpha = 색 농도(투명도)
# ax1.hist(np.random.randn(10), bins = 20, alpha =0.8)
# ax2.hist(np.random.randn(10))

# plt.show()

# 세로 막대 그래프
data = [30 , 90, 55, 60, 20]
plt.bar(range(len(data)), data)
         
plt.show()
 
# # 가로 막대 그래프
# err_data = np.random.rand(len(data))
#     # xerr : 편차, 에러값, 신뢰구간 등을 표시할때 유용함
# plt.barh(range(len(data)), data, alpha=0.5, xerr=err_data)
# plt.show()

# 원형 그래프 
# color는 리스트로도 줄수 있다.
# plt.pie(data, explode=(0, 0, 0.1, 0, 0), colors=['yellow', 'red', 'blue'])
# plt.show() 

# box 차트
# plt.boxplot(data)
# plt.show()

# 버블 차트
# n = 30
# np.random.seed(4)
# x = np.random.rand(n)
# y = np.random.rand(n)
# color = np.random.rand(n)
# scale = np.pi * (20 * np.random.rand(n)) ** 2
# plt.scatter(x, y, s=scale, c=color)
# plt.show()

# 시계열 데이터 
import pandas as pd

df = pd.DataFrame(np.random.randn(100, 4),
                  index = pd.date_range('1/1/2000', periods=100),
                  columns=list('ABCD'))

print(df)
df = df.cumsum()
plt.plot(df)
plt.show()
