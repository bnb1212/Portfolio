# 한글 형태소(단어로서 의미가 있는 최소한의 단위) 분석
# konlpy 라이브러리로 형태소 분석 가능. 품사 태깅
# corpu(말뭉치) : 자연어, 

from konlpy.tag import Kkma, Okt
kkma = Kkma()

print(kkma.sentences('여러분, 안녕하세요. 반갑습니다.'))
print()
print(kkma.nouns(u'오늘 폭염이 주춤했지만 일부지방은 폭염 특보 속에 35도 안팎의 찜통더위가 기승을 부렸는데요.자세한 날씨, YTN 중계차 연결해 알아보겠습니다.'))
print()
print(kkma.pos(u'오류보고는 실행환경, 에러메세지와 함께'))

print('----------------------------------------------------------------------')
okt = Okt()

aa = okt.pos('멋진 봄은 엄청 무더운 여름과 한들한들 시원한 가을의 중간 계절이다')
print(aa)
aa2 = okt.morphs('멋진 봄은 엄청 무더운 여름과 한들한들 시원한 가을의 중간 계절이다', stem=True) # 어근으로 출력. 멋진
print(aa2)
bb = okt.nouns('멋진 봄은 엄청 무더운 여름과 한들한들 시원한 가을의 중간 계절이다')
print(bb)

import nltk
parser_ko = nltk.RegexpParser("NP:{A.*>*<None>*}")
p_ko = parser_ko.parse(aa)
print(p_ko)

p_ko.draw()