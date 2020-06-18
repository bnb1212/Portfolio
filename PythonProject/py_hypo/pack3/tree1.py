'''============================================
DecisionTreeClassification / Regression (CART) 
의사결정트리분류 / 회귀
: 트리구조의 그래프를 사용하여 퇴적의 결정을 할 수 있도록 하는 알고리즘

- Information Gain : 지정된 속성이 얼마나 잘 training example들을 구분하는가에 대한 수치
- Entropy: example들의 집합에서의 혼잡성(impurity)을 나타냄. 노이즈의 정도를 수치로 표현. 0에 근사하면 우수

실습 필요 설치 패키지(pip install)

- graphviz (추가 설치와 환경변수 설정이 필요)
    <https://graphviz.org/_pages/Download/Download_windows.html>
- pydotplus

============================================'''

from sklearn import tree
import pydotplus
import collections
from sklearn.metrics import accuracy_score

# 변수 설정
x = [[180, 15], [177, 42], [156, 35], [174, 5], [166, 15]]
y = ['man', 'woman', 'woman', 'man', 'woman']

# model 생성 
model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=None, random_state=0)
print(model)

# 모델 학습
model.fit(x, y)

# 훈련 정확도 체크
print('훈련정확도 : {:.3f}'.format(model.score(x, y)))

# 분류 정확도 
pred = model.predict(x)
print(pred)
print('평가 정확도 : ', accuracy_score(y, pred))

# 예측
pred = model.predict(x)
print(pred)

# 새값으로 예측
newdata= [[171, 88]]
newpred= model.predict(newdata)
print('newpred:', newpred)


# 시각화
label_name = ['height', 'hair_length']
dot_data = tree.export_graphviz(model, feature_names=label_name, filled=True, rounded=True)
graph = pydotplus.graph_from_dot_data(dot_data)
colors = ('red', 'lightblue')
edges = collections.defaultdict(list)
                                
for e in graph.get_edge_list():
    edges[e.get_source()].append(int(e.get_destination()))

for e in edges:
    edges[e].sort()
    for i in range(2):
        dest = graph.get_node(str(edges[e][i]))[0]
        print('dest:', dest)
        dest.set_fillcolor(colors[i])
  
graph.write_png('tree.png')

from matplotlib.pyplot import imread
import matplotlib.pyplot as plt
img = imread('tree.png')
plt.imshow(img)
plt.show()