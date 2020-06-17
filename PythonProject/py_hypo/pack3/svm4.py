'''==========================================
BMI(체질량 지수)식을 이용해 무작위 자료를 작성 후 분류 모델에 적용
BMI = 몸무게 / 키(m)^2 
=========================================='''

import random 

random.seed(123)

def calc_bmi(h, w):
    bmi = w / (h / 100) ** 2
    if bmi < 18.5: return 'thin'
    elif bmi < 23: return 'normal'
    else: return 'fat'

# func test    
# print(calc_bmi(175, 25))

# bmi data 생성 후 파일로 저장    
fp = open('bmi.csv', 'w', encoding='utf-8')
fp.write('height,weight,label\n' )
# 무작위로 데이터 생성(5만개)
cnt = {'thin':0, 'normal':0, 'fat':0}
for i in range(50000): # 0만 더 붙여주면 큰데이터를 만들수있다
    h = random.randint(150, 200)
    w = random.randint(35, 100)
    label = calc_bmi(h, w)
    cnt[label] += 1
    fp.write('{0},{1},{2}\n'.format(h,w,label))
    
fp.close()
print('저장 완료', cnt)


# SVM bmi data분류
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

data_tbl = pd.read_csv('bmi.csv')
print(data_tbl.head(3))

# w, h에 대해 정규화하기 (0~1사이)
label = data_tbl['label']
w = data_tbl['weight'] / 100
h = data_tbl['height'] / 200
# 데이터 컬럼 합치기 
wh = pd.concat([w, h], axis=1)
print(wh.head(3))  # (50000, 2)
print(label[:3])  # (50000, )

# train / test dataset 분리(split)
data_train, data_test, label_train, label_test = train_test_split(wh, label)
print(data_train.shape, data_test.shape)

# model
# model = svm.SVC(C=10).fit(data_train, label_train)
# SVC의 개량종 LinearSVC(). SVC에 비해 속도가 향상되고 옵션이 다양해졌다. 무조건좋은건 아니다.
model = svm.LinearSVC(C=10).fit(data_train, label_train)
pred = model.predict(data_test)
print('실제값: ', label_test[:3])
print('예측값: ', label_test[:3])

# K-겹 교차검증 : Overfitting 방지용
from sklearn import model_selection
cross_vali = model_selection.cross_val_score(model, data_train, label_train, cv=5)
print('각각(5겹)의 검증 정확도: ',cross_vali)
print('평균(5겹)의 검증 정확도: ',cross_vali.mean())


# 분류 정확도 확인
ac_score = metrics.accuracy_score(label_test, pred)
print('정확도: ', ac_score) # 0.99592
cl_report = metrics.classification_report(label_test, pred)
print('분류 보고서: ', cl_report)

# 시각화
tbl = pd.read_csv('bmi.csv', index_col = 2)
print(tbl.head(3))

fig = plt.figure() # 이미지 저장 선언

def scatter_func(lbl, color):
    b = tbl.loc[lbl]
    plt.scatter(b['weight'], b['height'], c=color, label=lbl)
    
scatter_func('fat', 'lightcoral')
scatter_func('normal', 'springgreen')
scatter_func('thin', 'lightblue')
plt.legend()
plt.savefig('bmi_test.png')
plt.show()

