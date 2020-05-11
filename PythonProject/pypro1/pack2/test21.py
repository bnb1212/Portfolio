# 예외 처리 : try ~ except

def divide(a, b):
    return a/ b

c = divide(5,2)

print(c)

try:
    c = divide(5, 2)
    #c = divide(5, 0)
    
    aa = [1,2]
    print(aa[0])
    print(aa[3])
    
    f = open('c:/work/abc.txt')
    
except ZeroDivisionError:
    print("두번 째 숫자는 0을 주지 마세요")
    
except IndexError as e:
    print("참조 범위 오류")
    
except Exception as err:
    print('기타 에러 : ', str(err))


print('종료')    