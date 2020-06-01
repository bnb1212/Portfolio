# 웹 뉴스 정보로 워드 임베딩하여 유사 단어 파악하기
import pandas as pd
from konlpy.tag import Okt

# 1. okt 객체 만들기
okt = Okt()

# 2. daum news 읽어오기(파일)
with open('daumnews.txt', mode='r', encoding='utf8') as f:
    lines = f.read().split("\n")
    print(lines)
    
wordDic = {}

for line in lines:
    datas = okt.pos(line)
    print(datas)
    for word in datas:
        if word[1] == 'Noun':
#             print(word[0])
#             print(word[0] in wordDic)
            if not(word[0] in wordDic):
                wordDic[word[0]] = 0
            wordDic[word[0]] += 1
            
print(wordDic)

keys = sorted(wordDic.items(), key=lambda x:x[1], reverse=False)
print(keys)
wordList = []
countList = []

for word, count in keys[:20]:
    wordList.append(word)
    countList.append(count)
  
df = pd.DataFrame()
df['word'] = wordList
df['count'] = countList
print(df.head(3))

print('--------------------------------------------------------------')
results = []
with open('daumnews2.txt', mode='r', encoding='utf8') as fr:
    lines = fr.read().split('\n')
    
    for line in lines:
        datas = okt.pos(line, stem=True)
        # print(datas)
        imsi = []
        for word in datas:
            if not word[1] in ['Punctuation', 'Josa', 'Determiner', 'Alpha', 'Verb', 'Number']:
                imsi.append(word[0])
        imsi2 = (' '.join(imsi)).strip()
        results.append(imsi2)
        
print(results)

fileName = 'daumnews2.txt'

# df를 file로 저장
# with open(fileName, mode='w', encoding='utf8') as fw:
#     fw.write('\n')

# 워드 임베딩
from gensim.models import word2vec

# 간단한 예시
sentence = [['python', 'language', 'program', 'computer', 'say']]
model = word2vec.Word2Vec(sentence, min_count=1)

# 절대값 1에 가까울 수록 친밀함 
print(model.wv.most_similar('python')) 
print()

# 저장된 문서 daumnews2.txt를 읽어 유사 단어 파악
genObj = word2vec.LineSentence(fileName)

# word2 vec.LineSentence object
print(genObj)


# CBOW
# 나는 ~(중심단어) 간다
# 주변 단어를 이용해서 중심 단어를 유추

# Skip-Gram
# ~ 외나무다리 ~
# 중심 단어를 이용해서 주변 단어를 유추

# Word2Vec
# 여기서 size는 차원의 크기(이 구문은 100차원)
# window는 허용하는 주변 단어의 갯수
# min_count 최소 출현 빈도(미달된 것은 무시)
# sg(방법) -> 1 : Skip-Gram / 0 : CBOW
model = word2vec.Word2Vec(genObj, size=100, window=10, min_count=2, sg=1) 
print(model)

# 필요 없는 메모리 해제
model.init_sims(replace=True)

# 모델 저장 후 사용
try:
    model.save('daum_model.model')
    print("ok")
    
except Exception as e:
    print('err :',e)

# 모델 읽기
model = word2vec.Word2Vec.load('daum_model.model')

# 단어별 유사도 확인
print(model.wv.most_similar(positive='환자가'))
print(model.wv.most_similar(positive=['게'], topn=3))
print(model.wv.most_similar(positive=['생활속', '것'], negative=['하는']))


# 단어별 벡터를 만들어 유사도 출력 예제였다.