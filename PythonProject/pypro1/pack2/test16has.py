# 클래스의 포함관계로 로또 번호 출력
import random


class LottoBall:

    def __init__(self, num):
        self.num = num

    
# BallList에는 LottoBall 객체 45개가 들어감
class LottoMachine:

    def __init__(self):    
        self.ballList = []
        for i in range(1, 46):
            self.ballList.append(LottoBall(i))
    
    def selectBalls(self):
        # 섞기 전 출력
        # for a in range(45):
        #    print(self.ballList[a].num, end = ' ')
        random.shuffle(self.ballList)
        # 섞기 후 출력
        # for a in range(45):
        #    print(self.ballList[a].num, end = ' ')   
        return self.ballList[0:6]

    
class LottoUser:

    def __init__(self):
        self.machine = LottoMachine()  # 포함
        
    def playLotto(self):
        input('로또를 시작합니다. 행운을 빌며 !! 아무키나 누르세요')
        selectedBalls = self.machine.selectBalls()
        for ball in selectedBalls:
            print('%d ' % (ball.num))
        
if __name__ == '__main__':
    LottoUser().playLotto()
            
    
