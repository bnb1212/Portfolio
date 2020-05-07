# for target in object: ~ 

for i in [1, 2, 3, 4, 5]:
    print(i, end=' ')
else:
    print('for 수행')
    
print()
colors = ('r', 'g', 'b')
# colors = {'r', 'g', 'b'} -> set은 순서가 없당 
# colors = ['r', 'g', 'b'] 
for c in colors:
    print(c, end=' ')

print()
soft = {'java' :'웹용 언어', 'python':'접착 언어', 'C' :'시스템개발용' }
for i in soft.items():
    # print(i)
    print(i[0], ' ', i[1])

for k, v in soft.items():
    print(k, ' ', v)
print()
for k in soft.keys():
    print(k)
print()
for k in soft.values():
    print(k)
    
print()
for n in [2, 3]:
    print('--{}단'.format(n))
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print('{0}*{1}={2}'.format(n, i, n * i))
        
print()
li = ['a', 'b', 'c']
for ind, d in enumerate(li):  # enumerate 내장함수: 인덱스 값도 얻을수 있다.
    print(ind, ' ', d)
    
print()
datas = [1, 2, 3, 4, 5]
for i in datas:
    if i == 3: continue
    # if i ==3: break
    print(i, end=' ')
else:
    print('정상 종료 처리')
    
# 문자열 검색 후 단어 수 출력하기
import re
ss = '''
7일 국내 신종 코로나바이러스 감염증(코로나19) 확진자가 4명 증가, 사흘 연속 신규 확진자 5명 미만을 기록했다.
그러나 지난 사흘간 0명이던 국내 지역감염 사례가 나흘 만에 다시 나왔다.
중앙방역대책본부(방대본)은 7일 0시 기준 코로나19 확진자가 전날 0시보다 4명 늘어 총 1만810명으로 집계됐다고 발표했다.
방대본 발표일 기준으로 일일 신규 확진자 수는 4월 18일 18명으로 10명대에 진입한 이후, 20일째 20명 미만을 유지하고 있다.
최근에는 신규 확진자 증가세가 더욱 떨어져 지난 4일 8명으로 10명 아래로 떨어진 뒤 5일 3명, 6일 2명 등 5명 미만이 이어지고 있다.
신규 확진자 4명 중 1명은 국내 지역 발생으로 잠정 분류됐다. 국내발생 사례가 나온 것은 지난 3일 이후 나흘만으로, 경기에서 1명 발생했다. 3명은 해외유입 사례로, 검역 1명, 대전 1명, 충북 1명이다.
'''
    
print(ss)
# 정규 표현식으로 한글과 공백을 제외한 문자들을 없앰
ss2 = re.sub(r'[^가-힣\s]', '', ss)
print(ss2)
# 공백으로 구분
ss3 = ss2.split(' ')
print(ss3)
print(len(ss3))
# 중복 제거
sdata = set(ss3)
print(len(sdata))

cou = {}  # 단어의 발생횟수를 dic type으로 저장
for i in ss3: 
    if i in cou:
        cou[i] += 1
    else:
        cou[i] = 1
        
print(cou)
# dict 자료로 과일값 출력하기
price = {'사과':500, '수박':12000, '참외':600}
my = {'사과' : 2, '수박': 1}
bill = sum(price[f] * my[f] for f in my)
print('총 구매 가격: {}원'.format(bill))

print()
datas = [1, 2, 'a', True, 3]
li = [i * i for i in datas if type(i) == int]
print(li)
    
datas = {1, 1, 2, 2, 3}
se = {i * i for i in datas}
print(se)

id_name = {1: 'tom', 2: 'james'}
print(id_name)
name_id = {val:key for key, val in id_name.items()}
print(name_id)

print()
temp = [1, 2, 3]
for i in temp:
    print(i, end=' ')
print()
print([i for i in temp])
print({i for i in temp})
#    print((i for i in temp))
temp2 = list()
for i in temp:
    temp2.append(i)
print(temp2)
    
temp3 = [i + 10 for i in temp]
print(temp3)

print()
aa = [(1,2), (3,4), (5,6)]    
for a, b in aa:
    print(a+b)
    
# range함수
print(list(range(1,6)))
print(tuple(range(1,6)))
print(set(range(1,6)))

for i in range(6):
    print(i, end = " ")
print()
for i in range(2, 10):
    for j in range(1, 10):
        print('{}*{}={}'.format(i, j, i*j), end=' ')
    print()
    

