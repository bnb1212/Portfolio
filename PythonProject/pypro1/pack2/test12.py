# 모듈의 멤버로 클래스
aa = 10

def aa():
    pass

print(aa)
print()

class TestClass:
    kk = 1 # 멤버 변수(전역)
    
    def __init__(self):
        print('생성자')
        
    def __del__(self):
        print('소멸자')
    
    def printMsg(self): # 메소드(public)
        name = "한국인" # -지역변수
        print(name)
        print(self.kk)
    
test = TestClass() #생성자 호출. instance생성
print(test.kk)
print(TestClass.kk) # prototype(원형) 클래스의 멤버 직접 호출
print()

# 메소드 부르는 방법 2
test.printMsg() # 1) Bound Method Call
TestClass.printMsg(test) # 2) Unbound Method Call
print()

print(type(1)) 
print(type(test))
print(id(test))
print(id(TestClass))

# del test
# test.printMsg()