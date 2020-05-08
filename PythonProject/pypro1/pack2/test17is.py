# 클래스의 상속


class Animal:

    def __init__(self):
        print('Animal 생성자')

    def move(self):
        print("움직이는 생물")
        
        
class Dog(Animal): # 상속 받음 Animal
        
    # Java랑 다른점 : 해당 클래스의 생성자가 있을 경우 부모 생성자는 수행하지 않음
    def __init__(self):
        print('Dog 생성자')

    def my(self):
        print('나는 개')
    


dog1 = Dog()
dog1.my()
dog1.move()

print('=====' * 10)
class Cat(Animal):
    pass

cat1 = Cat()
cat1.move()

print('======= overrding ======')
class Parent:
    def PrintData(self): # 부모클래스에서 pass로 메소드를 비워두고 자식보고 채우라고 하는 이야기
        pass
    
class Child1(Parent):
    def PrintData(self):
        print("Child1에서 overriding함!")

class Child2(Parent):
    def PrintData(self):
        print("Child2에서 overriding함!")
             
    def abc(self):   
        print("Child2 고유 메소드")
        
        
c1 = Child1()
c1.PrintData()
c2 = Child2()
c2.PrintData()


print("=======다형성 =============")
# 자바랑 달리 형변환 이런거 따로 없이 그냥 변수에 담으면 된다.
kbs = c1
kbs.PrintData()
kbs = c2
kbs.PrintData()
kbs.abc()

print()
plist= [c1, c2]
for i in plist:
    i.PrintData()
    
