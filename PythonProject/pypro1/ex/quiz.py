from abc import *


# Employee =======================
# ABCMeta 클래스의 서브클래스는 추상클래스
class Employee(metaclass=ABCMeta):
    
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai
        
    # 봉급계산 추상메소드
    @abstractclassmethod
    def pay(self):
        pass
    
    # 데이터출력 추상메소드
    @abstractclassmethod
    def data_print(self):
        pass
    
    # 이름과 나이를 출력하는 함수
    def irumnai_print(self):
        print("이름 : {}, 나이 : {}, ".format(self.irum, self.nai), end="")
    
    
# Temporary ========================
class Temporary(Employee):
    
    def __init__(self, irum, nai, ilsu, ildang):
        
        # 부모생성자를 호출하여 값을 넘겨준다.
        super().__init__(irum, nai)
        
        # 멤벼변수들을 세팅한다.
        self.ilsu = ilsu
        self.ildang = ildang
        
    # 봉급계산 오버라이딩
    def pay(self):
        wage = self.ilsu * self.ildang
        return wage
    
    #데이터 출력 오버라이딩
    def data_print(self):
        super().irumnai_print()
        print("월급 : {}".format(self.pay()))


# Regular ============================
class Regular(Employee):

    def __init__(self, irum, nai, salary):
        super().__init__(irum, nai)
        self.salary = salary
        
    def pay(self):
        return self.salary
    
    def data_print(self):
        super().irumnai_print()
        print("급여 : {}".format(self.pay()))


# Salesman =============================
class Salesman(Regular):
    
    def __init__(self, irum, nai, salary, sales, commission):
        super().__init__(irum, nai, salary)
        self.sales = sales
        self.commission = commission
        
    def pay(self):
        real_amount = self.salary + (self.sales * self.commission)
        return real_amount
    
    def data_print(self):
        super().irumnai_print()
        print("수령액 : {}".format(self.pay()))
        

# Data Print ==============================
t = Temporary("홍길동", 25, 20, 15000)      
t.data_print()

r = Regular("한국인", 27, 3500000)
r.data_print()

s = Salesman("손오공", 29, 1200000, 5000000, 0.25)
s.data_print()
