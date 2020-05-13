# Thread 클래스를 상속받기

import threading, time

print('진행하다가...')


class MyClass(threading.Thread):

    def run(self):
        for i in range(1, 11):
            print('id:{} --> {}'.format(self.getName(), i))
            time.sleep(0.3)
            

ths = []
for i in range(2):
    th = MyClass()
    
    th.start()
    ths.append(th)
     
for th in ths:
    th.join()

print("프로그램 종료~")