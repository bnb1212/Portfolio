# BOW(Bag Of Word) : 문서가 가지는 모든 단어, 문맥, 순서를 무시하고
# 일괄적으로 단어에 대해 빈도수를 부여해 feature vector화 한다.

# count기반(CountVectorizer)과 TF-IDF(TfidfVectorizer)기반으로 나뉘어 진다.
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# CountVectorizer : 문서를 토큰리스트화한다. 각 문서에서 토큰의 출현빈도를 카운트, BOW 인코딩 벡터를 만든다.
# TfidfVectorizer : 단어의 가중치를 조정한 BOW 벡터(Vector)를 만든다. 자주나오는 단어에 가중치를 높인다.

count_vec = CountVectorizer(analyzer='word', min_df = 1)

contents = ["How to format my hard disk","Hard disk format format problems"]
aa = count_vec.fit_transform(contents)
print(aa)
print(count_vec.get_feature_names())
print(aa.toarray)
# [[1 1 1 1 1 0], 

print('-----------------------------------------------------------------------')
tfidf_vec = TfidfVectorizer(analyzer='word', min_df = 1)
bb = tfidf_vec.fit_transform(contents)
print(bb)
print(count_vec.get_feature_names())
print(bb.toarray)
