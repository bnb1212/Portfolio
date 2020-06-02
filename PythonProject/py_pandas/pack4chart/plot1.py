# 시각화
import numpy as np
import matplotlib.pyplot as plt

# 한글깨짐 방지
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False

# x축 y축에 list, tuple 가능. set은 안됨
x = ['서울', '인천', '수원']
y = [5, 3, 7]
# 
# plt.plot(x, y)
#  
# #최대 구간 최소 구간 설정
# plt.xlim([-1, 3])
# plt.ylim([0, 10])
#  
# # tick설정 (최소 최대 간격 ) 
# plt.yticks(list(range(0, 11, 3)))
# plt.show()

print()
data = np.arange(1, 11, 2)
# print(data)
# 
# plt.plot(data) # y축 값만 줌 
# plt.show()
# x = [0, 1, 2, 3, 4]
# for a, b in zip(x, data):
#     plt.text(a, b, str(b)) 

# plt.plot(data)
# plt.plot(data, data, c = 'r')
# plt.show()

x = np.arange(10)
y = np.sin(x)
print(x, y)

# plt.plot(x,y)

# 스타일 지정하기(b : blue / o : 산점도)
# plt.plot(x, y, 'bo')

# r : red / + : 십자모양
# plt.plot(y, 'r+')

# g: green / -- : 하선 / - : 실선 / -. : 길짧길짧 / :(콜론) : 점선
# linewidth(lw) : 선 두께 / markersize(ms) : 마커의 크기 / marker : 마커종류  
# plt.plot(x, y, 'go--', linewidth=3, markersize = 5)

# # Hold : 하나의 차트영역(figure)에 복수의 plot. 그림을 겹쳐 출력
x = np.arange(0, np.pi * 3, 0.1)
y_sin = np.sin(x) 
y_cos = np.cos(x)
# 
# plt.plot(x, y_sin, 'r')
# plt.plot(x, y_cos, 'b')
# plt.xlabel('x축')
# plt.ylabel('y축')
# plt.title('Hold 기능')
# # 범례)(legend)
# plt.legend(['sine', 'cosine'])
# plt.show()

# subplot : figure를 여러 개로 나눔
# plt.subplot(2, 1, 1)
# plt.plot(x, y_sin)
# plt.title('사인')
# 
# plt.subplot(2, 1, 2)
# plt.plot(x, y_cos)
# plt.title('코사인')

# plt.show()

irum = ['a', 'b', 'c', 'd', 'e']
kor = [80, 30, 43, 100, 95]
eng = [86, 54, 67, 68, 95]

plt.plot(irum, kor, 'ro--')
plt.plot(irum, eng, 'bs-')
plt.ylim([0, 100])
plt.title('시험 점수')
plt.legend(['국어', '영어'], loc =  4)
plt.grid(True)

# 차트를 이미지 파일로 저장 준비
fig = plt.gcf()
plt.show()

# 차트를 이미지로 저장
fig.savefig('aaa.png')

from matplotlib.pyplot import imread
img = imread('aaa.png')
plt.imshow(img)
plt.show()

