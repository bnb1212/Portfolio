# thread를 이용해 날짜 및 시간을 출력
import time

# 시간 출력하기
now = time.localtime()
print(now)
print('현재는 {}년 {}월 {}일'.format(now.tm_year, now.tm_mon, now.tm_mday))
print('{}시 {}분 {}초'.format(now.tm_hour, now.tm_min, now.tm_sec))
print('오늘은 {}요일이고 올해 {}번째 날'.format(now.tm_wday, now.tm_yday)) # 월요일 0, 화요일 1, ...
print()

import threading

def cal_show():
    now = time.localtime()
    print('현재는 {}년 {}월 {}일'.format(now.tm_year, now.tm_mon, now.tm_mday))
    print('{}시 {}분 {}초'.format(now.tm_hour, now.tm_min, now.tm_sec))
    
def myRun():
    while True:
        now2 = time.localtime()
        if now2.tm_min == 35: break
        cal_show()
        time.sleep(1)
        
th = threading.Thread(target=myRun)
th.start()

th.join()
print('프로그램 종료')