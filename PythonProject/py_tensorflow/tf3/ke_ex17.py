'''==============================================
iris dataset으로 분류 예측 모델 작성
ROC Curve 출력

ROC curve : Receiver Operation Characteristic Curve(수신자 판단 특성 곡선)
검사한 수치의 민감도(Sensitivity)와 1-특이도(Specificity)로 그려지는 Curve

=============================================='''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import roc_curve, auc
from numba.tests.test_array_exprs import ax2
from sklearn.preprocessing.tests.test_data import n_features

iris = load_iris()
# print(iris.DESCR)
x = iris['data']
print(x[:2])
y = iris['target']
print(y[:2], ' ', set(y))

names = iris['target_names']
print(names)
feature_names = iris['feature_names']
print(feature_names)

# Label 원핫
onehot = OneHotEncoder() 
# keras에는 to_categorical()이 있다. 
# numpy에는 np.eye()가 있다. 
# pandas에는 pd.get_dummies()가 있다.

print(y.shape)
y = onehot.fit_transform(y[:, np.newaxis]).toarray()
print(y.shape)
print(y[:2])

# feature 표준화
scaler = StandardScaler()
x_scale = scaler.fit_transform(x)
print(f"{x_scale[:2]}")

# split dataset 7:3
x_train, x_test, y_train, y_test = train_test_split(x_scale, y, test_size=0.3 , random_state=1)
n_features = x_train.shape[1]
n_classes = y_train.shape[1]
print(f"n_features: {n_features} / n_classes: {n_classes}")


# n개의 모델을 생성
def create_custom_model(input_dim, output_dim, out_nodes, n, model_name='model'):

    def create_model():
        model = Sequential(name=model_name)
        for _ in range(n):
            model.add(Dense(out_nodes, input_dim=input_dim, activation='relu'))
        
        model.add(Dense(output_dim, activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
        return model

    return create_model


models = [create_custom_model(n_features, n_classes, \
                               10, n, f'model_{n}') for n in range(1, 4)]

# for create_model in models:
#     print()
#     create_model().summary()

history_dict = {}

for create_model  in models:
    model = create_model()
    histories = model.fit(x_train, y_train, batch_size=5, epochs=50, verbose=0, validation_split=0.3)
    score = model.evaluate(x_test, y_test, verbose=0)
    print(f"test dataset loss: {score[0]}")
    print(f"test dataset accuracy: {score[1]}")
    history_dict[model.name] = [histories, model]
    
print(history_dict)

# 시각화
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
'''
for model_name in history_dict:
#     print('h_d : ', history_dict[model_name][0].history['acc'])
    val_acc = history_dict[model_name][0].history['val_acc']
    val_loss = history_dict[model_name][0].history['val_loss']
    ax1.plot(val_acc, label = model_name)
    ax2.plot(val_loss, label = model_name)
    ax2.set_ylabel('validation acc')
    ax2.set_ylabel('validation loss')
    ax2.set_xlabel('epochs')
    
    ax1.legend()
    ax2.legend()
plt.show()
'''

'''
# ROC Curve : 모델 성능을 확인 ( 분류기에 대한 성능 평가 기법 중 하나 )
plt.figure()
plt.plot([0,1],[0,1], 'k--')
for model_name in history_dict:
    model = history_dict[model_name][1]
    y_pred = model.predict(x_test)
    fpr, tpr, _ = roc_curve(y_test.ravel(), y_pred.ravel())
    plt.plot(fpr, tpr, label=f"{model_name}, AUC value:{auc(fpr, tpr):.3f}")
    
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('ROC Curve')
plt.show()

'''

# KerasClassifier를 이용해 model n개를 교차 검증 수행 가능
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score  # k-fold 교차검증
create_model = create_custom_model(n_features, n_classes, 10 , 3)

estimator = KerasClassifier(build_fn=create_model, epochs=50, batch_size=10, verbose=2)
scores = cross_val_score(estimator, x_scale, y, cv=10)
print(f'accuracy mean: {scores.mean():0.2f} (+/-{scores.std():0.2f})')

# 위 결과 모델3(4개의 레이어 사용)이 가장 우수한 모델로 판정
model = Sequential()
model.add(Dense(10, input_dim=4, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])

model.fit(x_train, y_train, epochs=50, batch_size=5, verbose=2)
print(model.evaluate(x_test, y_test))

y_pred = np.argmax(model.predict(x_test), axis=1).reshape(-1, 1)
print('예측값: ', y_pred.ravel())
real_y = np.argmax(y_test, axis=1).reshape(-1,1)
print('실제값: ', real_y.ravel())
print('분류 실패 수 :', (y_pred.ravel() != real_y.ravel()).sum())

print()
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import metrics

print(confusion_matrix(real_y, y_pred))
print(metrics.accuracy_score(real_y, y_pred))
print(classification_report(real_y, y_pred))
      
# 새 값으로 분류
new_x = [[5.1, 3.5, 1.4, 0.2], [1.9, 3.1, 1.4, 1.2], [4.9, 3., 1.4, 0.2]]
new_x = StandardScaler().fit_transform(new_x)
new_pred = model.predict(new_x)
print(np.argmax(model.predict(new_pred, axis=1)).reshape(-1, 1).flatten())