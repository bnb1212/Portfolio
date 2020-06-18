'''==========================================
SVM으로 얼굴 이미지 분류
==========================================='''

from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
from sklearn.metrics._classification import classification_report

faces = fetch_lfw_people(min_faces_per_person=60)
print(faces) # {'data':array([[112. , 134. ...
print(faces.target_names)
print(faces.images.shape)

# 3행 5열로 데이터 시각화
fig, ax= plt.subplots(3, 5)
print(fig) # 기본크기 : 640 x 480
print(ax.flat, ' ', len(ax.flat)) # 3 * 5 = 15
for i, axi in enumerate(ax.flat):
    axi.imshow(faces.images[i], cmap='bone')
    axi.set(xticks=[], yticks=[], xlabel=faces.target_names[faces.target[i]])
plt.show()

# PCA 주성분 분석
# 이미지 전체가 아니라 주요 특징만을 추출한 이미지로 분류 작업을 수행
from sklearn.svm import SVC
from sklearn.decomposition import PCA
# 연속적인 작업을 위한 pipeline 패키지
from sklearn.pipeline import make_pipeline

# 이미지 차원 축소
m_pca = PCA(n_components=150, whiten = True, random_state=0) # whiten - 스케일 조정
m_svc = SVC()
model = make_pipeline(m_pca, m_svc)
print(model)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(faces.data, faces.target, random_state=1)
print(x_train.shape)
print(y_train.shape)

model.fit(x_train, y_train)

yfit = model.predict(x_test)
print(yfit)

# 분류 보고서
from sklearn.metrics import classification_report
print(classification_report(y_test, yfit, target_names=faces.target_names))

# 분류 정확도
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
mat = confusion_matrix(y_test, yfit)
print(mat)
print('분류 정확도 : ', accuracy_score(y_test, yfit))

# test 이미지 중 일부 자료로 예측한 값과 비교를 위한 시각화 
# plt.imshow(x_test[0].reshape(62, 47), cmap='bone')
# plt.show()

fig, ax = plt.subplots(4, 6)
# print(ax)
for i, axi in enumerate(ax.flat):
    axi.imshow(x_test[i].reshape(62, 47), cmap='bone')
    axi.set(xticks=[], yticks=[])
    axi.set_ylabel(faces.target_names[yfit[i]].split()[-1],
                    color='black' if yfit[i] == y_test[i] else 'red')
    fig.suptitle('pred', size=15)
plt.show() # 제대로 나오면 검은색, 잘못나오면 빨간 색

# 클래스들 간의 오차 행렬을 시각화
import seaborn as sns

sns.heatmap(mat.T, square=True, annot=True, cbar = False,
            xticklabels=faces.target_names, 
            yticklabels=faces.target_names)
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()
    