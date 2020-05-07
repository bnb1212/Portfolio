# 함수 계속
# 인수 키워드 매핑


def ShowGugu(start, end=5):
    for dan in range(start, end + 1):
        print(str(dan) + '단 출력')

        
ShowGugu(2, 3)
print()
ShowGugu(3)
print()
ShowGugu(start=2, end=4)
print()
ShowGugu(end=4, start=3)
print()

# 가변인수 
print('\n가변인수')


def func1(*ar):  # *을 넣으면 인수를 가변적으로 여러개 받을 수 있다 
    print(ar)
    for i in ar:
        print('음식 : ' + i)


func1('비빔밥', '공깃밥', '주먹밥')
 
print()


def func2(a, *ar): 
    print(a)
    print(ar)

    
func2('비빔밥', '공깃밥', '주먹밥')

print()


def func3(a, b, *v1, **v2):  # * 하나는 튜플, ** 두개는 딕셔너리(dictionary)
    print(a, b)
    print(v1)
    print(v2)

    
func3(1, 2)
print()
func3(1, 2, 3, 4, 5)
print()
func3(1, 2, 3, 4, 5, m=6, n=7)
print()

print("=====" * 10)


# closure 클로저
def out():  # 아직 클로저는 안나오는 예시
    count = 0

    def inn():
        nonlocal count
        count += 1
        return count

    print(inn())


out()
out()


def outer():  # 클로저 사용예시
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner  # 이 부분을 클로저라고 함
    # 함수 내부에 함수를 만들고, 그 함수의 주소를 리턴

    
add1 = outer()
print(add1())
print(add1())
print(add1())

add2 = outer()
print(add2())
print(add2())

print('수량 * 단가 * 세금 결과 출력 ==========')


def outer2(tax):

    def inner2(su, dan):
        amount = su * dan * tax
        return amount

    return inner2


a1 = outer2(0.1)
# print(id(a1))

result1 = a1(5, 1000)
print(result1)
result2 = a1(10, 20200505)
print(result2)
print()

a2 = outer2(0.05)
result3 = a2(5, 1000)
print(result3)

print('=== 일급 함수 ( 함수 안에 함수, 인자로 함수 전달, 반환 값이 함수 ) ====')


def fun1(a, b):
    return a + b


fun2 = fun1
print(fun2(3, 4))

print()


def fun3(func):

    def fun4():
        print("난 내부 함슈~~")

    fun4()
    return func


mbc = fun3(fun1)  # fun3의 반환이 fun1 이므로 mbc는 fun1이고, fun3은 호출되었기때문에 내부의 fun4를 실행하고 fun1을 리턴
print(mbc(3, 4))

# Lambda 함수
# lambda (argument) : (return)
print("=====" * 10)


def Hap(x, y):
    return x + y


print(Hap(1, 2))

print((lambda x, y : x + y)(1, 2))

aa = lambda x, y : x + y

print(aa(3, 4))

kbs = lambda a, su = 10: a + su 
print(kbs(5))
print(kbs(5, 6))

print()
sbs = lambda a, *tu, **di: print(a, tu, di)
sbs(1, 2, 3, m=4, n=5)

print()
li = [lambda a, b: a + b, lambda a, b: a * b]
print(li[0](3, 4))
print(li[1](3, 4))

# 다른 함수에서 람다 사용
print(list(filter(lambda a:a < 5, range(10))))
print(list(filter(lambda a:a % 2, range(10))))
print()

# 함수 장식자(decorator)
print('===== 함수장식자 =====')


def make2(fn):
    return lambda:'안녕 ' + fn()


def make1(fn):
    return lambda:'반가워 ' + fn()


def hello():
    return "홍길동"


hi = make2(make1(hello))
print(hi())  # decorator 사용 X

print()


@make2
@make1
def hello2():
    return '신기해'


print(hello2())

print('--------')
hi2 = hello2()
print(hi2)
hi3 = hello2
print(hi3())

# 재귀 함수
print('===== 재귀 함수 ======')


def CountDown(n):
    if n == 0:
        print("완료")
    else:
        print(n, end=' ')
        CountDown(n - 1)  # <=== 자기 자신을 호출하는 중

        
CountDown(5)

print()
def tot(n):
    if n == 1:
        print('탈출')
        return 1
    return n + tot(n - 1)

result = tot(10)
print('합은 ' + str(result))

print() # 5! 팩토리얼
def facto(a):
    if a == 1: return 1
    print(a)
    return a * facto(a - 1)
result2 = facto(5)

print('5! : ' + str(result2))    


