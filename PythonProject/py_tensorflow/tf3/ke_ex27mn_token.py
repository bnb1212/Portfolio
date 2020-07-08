'''================================
텍스트의 토큰화를 통해 컴퓨터가 인지할 수 있도록 텍스트를 숫자화
================================'''

import numpy as np
# Corpus를 Token화(Tokenize) => 토큰 : 단어별, 문장별, 형태소 별로 텍스트를 나눌때 가장 작은 단위
# 단어 집합 :vocabulary

# 단어 수준으로 인덱싱
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, LSTM, Embedding
from nltk.util import pad_sequence
from keras_preprocessing.sequence import pad_sequences
samples = ['The cat say on the mat.', 'The dog ate my homework.']

# 직접 토큰 분리 ---------------------------------
token_index = {}
for sam in samples:
    for word in sam.split():  # sep = ' '
        if word not in token_index:
            print(word)
            token_index[word] = len(token_index)
            
print(token_index)
# {'The': 0, 'cat': 1, 'say': 2, 'on': 3, 'the': 4, 'mat.': 5, 'dog': 6, 'ate': 7, 'my': 8, 'homework.': 9}

# Tokenizer로 토큰 분리 ----------------------------
tokenizer = Tokenizer()  # 속성 : num_words = 5
tokenizer.fit_on_texts(samples)
token_seq = tokenizer.texts_to_sequences(samples)  # 텍스트를 정수 인덱싱한 후 list type으로 반환
print(token_seq)

print()
token_mat = tokenizer.texts_to_matrix(samples, mode='count')  # mode='count' : 갯수를 세어준다, 'binary', tfidf : 가중치 ,'frequency' : 빈도수
print(token_mat)
                                     
word_index = tokenizer.word_index
print(word_index)
print(f'found {len(word_index)} unique tokens')
print(tokenizer.word_counts)
print(tokenizer.document_count)
print(tokenizer.word_docs)

from tensorflow.keras.utils import to_categorical
token_onehot = to_categorical(token_seq[0], num_classes=6)
print(token_onehot)

print('-----------------------------------------------')
text = '우리 공부하러 갈래 언어는 자바 파이썬 자바 만세'
t = Tokenizer()
t.fit_on_texts([text])
# 입력으로 [text]가 아닌 text를 넣을 경우 한 글자 단위 인코딩이 된다.
print(t.word_index)

print()
docs = ['먼저 텍스트의 각 단어를 나누어 토큰화 한다.',
        '텍스트의 단어로 토큰화 해야 딥러닝에서 인식된다.',
        '토큰화한 결과는 딥러닝에서 사용할 수 있다.'
        ]
token = Tokenizer()
token.fit_on_texts(docs)
print('단어 카운트 :', token.word_counts)
print('문장 카운트 :', token.document_count)
print('각 단어가 몇 개의 문장에 포함되어 있는가 :', token.word_docs)
print('각 단어에 매겨진 인덱스 값 :', token.word_docs)

print()
# 텍스트를 읽고 긍정, 부정 분류 예측
docs = ['너무 재밌네요', '최고에요', '참 잘 만든 영화에요', '추천하고 싶은 영화네요', '한번 더 보고싶네요',
      '글쎄요', '별로네요', '생각보다 지루합니다.', '연기가 좋지 않아요', '재미없어요']
classes = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
token = Tokenizer()
token.fit_on_texts(docs)
print(token.word_index)
x = token.texts_to_sequences(docs)
print('토큰 정수 인덱스 결과:', x)

# 토큰 정수 인덱스 결과의 길이를 동일(padding)
padded_x = pad_sequences(x, maxlen=4)
print('패딩 후 ', padded_x)

# model
word_size = len(token.word_index) + 1

model = Sequential()
# Embedding : 자연어를 수치화
model.add(Embedding(word_size, 8, input_length=4))
# model.add(Flatten())
model.add(LSTM(32))
model.add(Dense(1, activation='sigmoid'))

print(model.summary())

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(padded_x, classes, epochs=20, verbose=1)
print('acc:', model.evaluate(padded_x, classes)[1])
print()
print(f'pred:{model.predict(padded_x)}')

