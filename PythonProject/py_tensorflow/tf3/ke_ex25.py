'''==================================================
RNN 순환신경망
자연어 처리(NLP) : 음성이나 텍스트를 인식하고 분석처리하기에 효과적인 네트워크
텍스트 분류, 품사 태깅, 이미지 개선, 기계 번역, 챗봇, 새로운 글(소리) 작성 ...
==================================================='''

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, LSTM, GRU
from tensorflow.keras.layers import Dense

model = Sequential()

# model.add(SimpleRNN(3, input_shape=(2, 10)))  # 2행 10열 자료로 출력 3개 수행

# print(model.summary())

# model.add(SimpleRNN(3, input_shape=(2, 10)))
# model.add(SimpleRNN(3, input_length=2, input_dim=10))
model.add(LSTM(3, input_shape=(2, 10)))

print(model.summary())

print()
model = Sequential()

# model.add(SimpleRNN(3, batch_input_shape=(8, 2, 10)))
model.add(LSTM(3, batch_input_shape=(8, 2, 10)))
# (8: batch_size 2: Sequence_size, 10: 출력수)

print(model.summary())

print()
model = Sequential()
model.add(LSTM(3, batch_input_shape=(8, 2, 10), return_sequences=True))
model.add(Dense(2, activation='softmax'))
print(model.summary())


