# python의 GIL 정책으로 인해 thread 작동이 제대로 안되는 경우가 발생.
# multiprocessing을 위한 클래스를 별도 제공

from multiprocessing import Pool
import time
import os


def Func(x):
    print('값', x, "에 대한 작업 pid=", os.getpid())  # 현재 프로세스 id를 얻음
    time.sleep(1)
    return x * x


if __name__ == "__main__":
    startTime = int(time.time())
    
    # 일반적 =======================================================
    # for i in range(0, 10):  # 일반적인 방법으로 함수를 호출
    #    print(Func(i))
        
    # endTime = int(time.time())
    # print('총 작업 시간 : ', (endTime - startTime))
        
    # 병렬처리 ==============================================
    p = Pool(3)  # multiprocessing 방법으로 함수를 호출 ( 3~5 사이를 권장 )
    print(p.map(Func, range(0,10)))
    
    endTime = int(time.time())
    print('총 작업 시간 : ', (endTime - startTime))
