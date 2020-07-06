'''==============================================
RNN으로 텍스트 생성
============================================='''
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
from tensorflow.keras.layers import Embedding, Dense, SimpleRNN, LSTM
from tensorflow.keras.models import Sequential

text = '''경마장에 말이 뛰고 있다
그의 말이 법이다
가는 말이 고와야 오는 말이 곱다
'''

# 텍스트를 Sequence화
tok = Tokenizer()
tok.fit_on_texts([text])
encoded = tok.texts_to_sequences([text])[0]
# print(encoded) # [2, 1, 3, 4, 1, 5, 6, 1, 7, 8, 1, 9]

print(tok.word_index)

vocab_size = len(tok.word_index) + 1
print(f'단어 집합의 크기 : {vocab_size}')  # 10

# Train data
sequences = list()
for line in text.split('\n'):
    encoded = tok.texts_to_sequences([line])[0]
    print(encoded)
    for i in range(1, len(encoded)):
        sequ = encoded[:i + 1]
        # print(sequ)
        sequences.append(sequ)
        
print(sequences)
print(f'샘플 수 : {len(sequences)}')  # 10

# [[2, 1], [2, 1, 3], [2, 1, 3, 4], [5, 1], [5, 1, 6], [7, 1], [7, 1, 8], [7, 1, 8, 9], [7, 1, 8, 9, 1], [7, 1, 8, 9, 1, 10]]
# feacture는 앞에오는 항목들, label은 리스트 마지막에 위치한 항목

# feature, label 구하기
print(max(len(i) for i in sequences))  # 6:샘플 중 가장 길이가 긴 값

from tensorflow.keras.preprocessing.sequence import pad_sequences
max_len = max(len(i) for i in sequences)

sequences = pad_sequences(sequences, maxlen=max_len, padding='pre')
print(sequences)  # [[ 0 0 0 0 2 1] [ 0 0 0 2 1 3]
# 각 샘플의 마지막 요소값을 레이블로 사용하기위해 분리
sequences = np.array(sequences)
x = sequences[:, :-1]  # feature
y = sequences[:, -1]  # label
print(x[:3])
print(y[:3])

# 인코딩 : 고차원의 벡터를 저차원으로 압축처리 
from tensorflow.keras.utils import to_categorical
y = to_categorical(y, num_classes=vocab_size)
# print(y)

model = Sequential()
# 
model.add(Embedding(vocab_size, 32, input_length=max_len - 1))
model.add(LSTM(32))
model.add(Dense(32, activation='relu'))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x, y, epochs=200, verbose=2, batch_size=32)
print(model.evaluate(x, y))


# 모델이 정확하게 예측하는지 함수 작성
def sentence_generation(model, t, current_word, n):
    init_word = current_word
    sentence = ''
    for _ in range(n):
        encoded = t.texts_to_sequences([current_word])[0]  # 현재 단어에 대한 정수 인코딩
        encoded = pad_sequences([encoded], maxlen=max_len - 1, padding='pre')
        result = np.argmax(model.predict(encoded), axis=-1)
        print(result)
        for word, index in t.word_index.items():
#             print(f'word:{word} index:{index}')
            if index == result:
                break
        current_word = current_word + ' ' + word # 현재 단어 + 예측 단어
        sentence = sentence + ' ' + word
        
    sentence = init_word + sentence
    return sentence
    
print(sentence_generation(model, tok, '경마', 1))
print(sentence_generation(model, tok, '경마장에', 1))
print(sentence_generation(model, tok, '경마장에', 5))
print(sentence_generation(model, tok, '그의', 2))
print(sentence_generation(model, tok, '가는', 3))
print(sentence_generation(model, tok, '가는', 5))

