
'''
여러줄
주
석
'''

# 한 줄 주석
var1 = '안녕'
print(var1)
var1 = 5;
print(var1);
var1 = '변수선언시 type은 저장되는 자료에 의해 결정됨'
print(var1)

a = 10
b = 20.1
c = b
print(a, b, c)
print('주소 출력 : ', id(a), id(10), id(b), id(20.1), id(c))
print(a is b, a == b)  # is : 주소 비교 , == 값비교
print(b is c, b == c)

print()
A = 1; a = 2
print(A, ' ', a)

# 예약어
print()
import keyword
print('예약어: ', keyword.kwlist)

# 진법 연습
print('\n진법')
print(10, oct(10), hex(10), bin(10))  # 10 0o12 0xa 0b1010
print(10, 0o12, 0xa, 0b1010)  # 10 10 10 10

# 자료형
print('자료형')
print(7, type(7))
print(7.1, type(7.1))
print(7 + 3j, type(7 + 3j))
print(True, type(True))
print('kbs', type('kbs'))

print((1,), type((1,)))
print([1], type([1]))
print({1}, type({1}))
print({'k':1}, type({'k':1}))

print(isinstance(a, int))
print(isinstance(a, float))

print('============ 연산자 =================')
v1 = 2
v1 = v2 = v3 = 5
print(v1, v2, v3)
v1 = 1, 2, 3
print(v1)  # (1, 2, 3) 자동으로 tuple이 된다
v2, v3 = 10, 20
print(v2, v3)

v1, v2 = 10 , 20
v2, v1 = v1, v2
print(v1, v2)

print('============ packing =================')
# v1, *v2 = [1,2,3,4,5]
* v1, v2 = 1, 2, 3, 4, 5
print(v1)
print(v2)
* v1, v2, v3 = 1, 2, 3, 4 , 5
print(v1)
print(v2)
print(v3)

print('============ 연산자 ===================')
print(5 + 3, 5 - 3, 5 * 3)
print(5 / 3, 5 // 3, 5 % 3, 5 ** 3)
print(divmod(5, 3))  # 몫과 나머지를 tuple로 담음

print()
print(3 + 4 * 5, (3 + 4) * 5)

print('--- 관계 연산 : ' , end=' ')
print(5 > 3, 5 == 3, 5 != 3)

print('--- 논리 연산 : ' , end=' ')
print(5 > 3 and 4 <= 3, not(5 >= 3))

print("--- 문자열 더하기 : ", end=" ")
print("한" + "국" + "만세")
print("한국" * 20)

print("누적")
a = 10
a = a + 1
a += 1  # ++ -- X 증감 연산자 불가
print(a)
print(a * -1, -a, - -a)

# 파이썬에서는 0만 False 나머지는 True값을 가진다
print('bool 처리 : ' , bool(0), bool(1), bool(True), bool(False))
print('bool 처리 : ' , bool(100), bool(-10), bool(None), bool(''), bool([]), bool({}))

# 파이썬의 이스케이프와 소문자 r의 선행으로 이스케이프 막기
print()
print(r'kbs\tbs')
print(r'kbs\nbc')

# String Format
print('**' * 20)
print(format(1.2345, '10.3f')) # 10자리 소수점 3까지
print('나이가 %d입니다.' % 22)
print('나이가 %s입니다.' % '스물')
print('나이가 %d입니다. %s' % (22, '스물'))
print('나이가 %s입니다 %s %f' % (22, '스물', 22.5))
print('이름은 {} 나이는 {}'.format('하하', 33))
print('이름은 {0} 나이는 {1}'.format('하하', 33))
print('이름은 {1} 나이는 {0}'.format('하하', 33))
print('이름은 {1} 나이는 {0} {1} {1}'.format('하하', 33))
