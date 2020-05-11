kor = 100

def abc():
    print("난 모듈의 멤버인 함수")
    
class my:
    kor = 90
        
    def abc(self):
        print("메소드")
            
    def show(self):
        kor=77
        print(kor)
        print(self.kor) # ->90
        self.abc()
        abc()
        
            
m = my()
m.show()

print("=====" * 10)
class Our:
    a = 1
    
o1 = Our()
print(o1.a)
o1.a = 2
print(o1.a)

print()
o2 = Our()
print(o2.a)
o2.b = 10
print(o2.b)

# print(o1.b) # err 
print(Our.a)
# print(Our.b) # err

# 클래스는 새로운, 나만의 type을 만드는 것
print(type(o1))

class Singer:
    titlesong = 'desperado'
    
    def sing(self):
        msg="노래는"
        print(msg, self.titlesong, '랄랄라~~')
        

yuna = Singer()
yuna.sing()

print()
redvelvet = Singer()
redvelvet.sing()
redvelvet.titlesong = "뻘건맛"
redvelvet.sing()
redvelvet.co = 'SM'
print("소속사 : " + redvelvet.co)
print()
yuna.sing()
print


