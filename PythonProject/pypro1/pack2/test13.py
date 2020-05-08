# 원형 클래스 (prototype)
class Car:
    handle = 0
    speed = 0
    
    def __init__(self, name, speed):
        self.speed = speed
        self.name = name
    
    def showData(self):
        km = "킬로미터";
        msg = "속도" + str(self.speep) + km
        return msg

    
print(Car.handle)
print(Car.speed)
print(Car.name)
    
# 인스턴스 생성
print()
car1 = Car('tom', 10)
print(car1.handle, car1.name, car1.speed)
car1.color = '검정'
print('car1.color: ', car1.color)

car2 = Car('james', 20)
print(car2.handle, car2.name, car2.speed)

# 각 인스턴스의 객체들
print()
print(id(Car), ' ', id(car1), ' ', id(car2))
print()
print(car1.showData())
print(car2.showData())
car1.speed = 88 
car1.speed = 100
print(car1.showData()) 
print(car2.showData()) 

car1.handle = 1
print(car1.handle)
print(car2.handle)
