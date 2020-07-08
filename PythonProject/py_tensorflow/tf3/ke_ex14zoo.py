'''====================================================
softmax로 다항분류 - 동물 type 분류
===================================================='''
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
import numpy as np

xy = np.loadtxt("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/zoo.csv", delimiter=',')
print(xy[0], xy.shape)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]
print(x_data[:1])
print(y_data[:1], set(y_data.ravel()))

nb_classes = 7
# y_one_hot = to_categorical(y_data, num_classes=nb_classes)
# print(y_one_hot[:1])

# 모델 생성
model = Sequential()
model.add(Dense(32, input_shape=(16,), activation="relu"))
model.add(Dense(32, activation="relu"))
model.add(Dense(nb_classes, activation="softmax"))
model.summary()

# 컴파일
# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics='accuracy')
# sparce_categorical_crossentropy : 원핫인코딩 안해도됨 이거 쓰면
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')

# history = model.fit(x_data, y_one_hot, epochs=100, batch_size=10,
#                     validation_split=0.2, verbose=2)
# 
# print(f"eval :{model.evaluate(x_data, y_one_hot)}")

history = model.fit(x_data, y_data, epochs=100, batch_size=10,
                    validation_split=0.2, verbose=2)

print(f"eval :{model.evaluate(x_data, y_data)}")

# 시각화
hist_dict = history.history
print(hist_dict)
loss = hist_dict['loss']
val_loss = hist_dict['val_loss']
accuracy = hist_dict['accuracy']
val_accuracy = hist_dict['val_accuracy']

import matplotlib.pyplot as plt
plt.plot(loss, 'b-', label='train_loss')
plt.plot(val_loss, 'r--', label='val_loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

plt.plot(accuracy, 'b-', label='train_loss')
plt.plot(val_accuracy, 'r--', label='val_loss')
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend()
plt.show()

print()
pred_data = x_data[:5]
pred = np.argmax(model.predict(pred_data), axis=-1)
print(pred)

pred_datas = x_data[:5]
preds = [np.argmax(i) for i in (model.predict(pred_datas))]
print(pred)
print(f"예측값들 :{preds}")
print(f"실제값들 :{y_data[:5].flatten()}")

# 새로운 데이터로 분류 참여
new_data = np.array([[1., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 12., 0., 0., 0.,]])
print(np.argmax(model.predict(new_data)))