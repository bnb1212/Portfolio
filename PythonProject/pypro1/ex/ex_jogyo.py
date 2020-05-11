# 추상클래스
from abc import *

class Employee(metaclass=ABCMeta):
    #ABCMeta 클래스의 서브클래스는 추상클래스

    # 부모 클래스 생성자 이걸로 자식클래스의 irum nai를 가져온다.
    def __init__(self,irum,nai):
        self.nai = nai
        self.irum = irum
    
    # 이름과 나이를 출력하는 함수
    def display_irumnai_print(self):
        print('이름 : ',self.irum, '나이 : ',self.nai ,end=' ')
    
    
    # 봉급계산 추상메소드
    @abstractclassmethod
    def pay(self):
        pass
    
    #데이터출력 추상메소드
    @abstractclassmethod
    def data_print(self):
        pass

# 계약직 클래스
class Temporary(Employee):
    
    #멤버변수들
    ilsu = 0
    ildang = 0
    
    # 계약직의 생성자 이걸로 값들을 받아온다
    def __init__(self,irum,nai,ilsu,ildang):
        
        #부모생성자를 호출하여 값을 넘겨준다.
        super().__init__(irum, nai)
        
        # 멤벼변수들을 세팅한다.
        self.ilsu = ilsu
        self.ildang = ildang
    
    # 봉급계산 오버라이딩
    def pay(self):
        return self.ilsu*self.ildang
    
    #데이터 출력 오버라이딩
    def data_print(self):
        super().display_irumnai_print()
        print('월급 : ',self.pay())
        

# 정규직 사원 클래스
class Regular(Employee):
    
    #멤버변수
    salary = 0
    
    
    # 정규식 사원 클래스 생성자
    def __init__(self,irum,nai,salary):
        #마찬가지로 부모 생성자 호출
        super().__init__(irum,nai)
        #멤버변수 세팅        
        self.salary = salary    
        
    # 봉급계산 오버라이딩
    def pay(self):        
        return self.salary
        
    # 데이터출력 오버라이딩   
    def data_print(self):
        super().display_irumnai_print()
        print('급여 : ',self.pay())

# 세일즈 사원 클래스
class Salesman(Employee):
    
    #멤버변수 초기화
    salary = 0
    sales = 0
    commission = 0
    
    # 생성자
    def __init__(self,irum,nai,salary,sales,commission):
        #부모생성자 호출
        super().__init__(irum,nai)
        
        # 멤버변수 세팅
        self.salary = salary
        self.sales = sales
        self.commission = commission
        
    # 봉급
    def pay(self):
        return self.salary + (self.sales * self.commission)
    
    # 출력
    def data_print(self):
        super().display_irumnai_print()
        print('수령액: ',self.pay())
        
        
# 실행
t = Temporary('홍길동',25,20,15000)
r = Regular('한국인',27,3500000) 
s = Salesman('손오공',29,1200000,5000000,0.25)

t.data_print()
r.data_print()
s.data_print()






    
    