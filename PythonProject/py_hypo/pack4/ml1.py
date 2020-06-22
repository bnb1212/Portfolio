'''=================================================
# 단층 Perceptron은 XOR 분류를 하지 못함. 층(Layer)을 늘리면 가능해진다.
# 이를 Multi Layer Perceptron, MLP라고 한다.
================================================='''
import numpy as np
from sklearn.linear_model import Perceptron

# 단일 퍼셉트론
feature = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
label = np.array([0,1,1,0]) 
# print(feature)

#- 모델 학습
ml = Perceptron(max_iter = 1000).fit(feature, label)
# print(ml.predict(feature)) # 해결이 안된다.

print('\n====================================\n')
# 다층 신경망(MLP) 사용
from sklearn.neural_network import MLPClassifier
# 기본
# ml2 = MLPClassifier(hidden_layer_sizes=100).fit(feature, label)

# verbose : Verbosity mode. 기본 값은 0 , 1을 주면 진행과정을 보여준다
# ml2  = MLPClassifier(hidden_layer_sizes=5, verbose=1).fit(feature, label)

# 노드/레이어 갯수가 늘어나면 자연히 연산도 늘어남
# 
ml2  = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=100, learning_rate_init=0.01, random_state=1, verbose=0).fit(feature, label)
print(ml2)

print(ml2.predict(feature))
