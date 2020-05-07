# 정규 표현식
import re
from bottleneck.slow.reduce import ss

ss = '1234 abc nbc 가나다 ABC_555_6 a b 123'
print(ss)

# ## 패턴을 줄 때 r을 빼먹지 말자
print(re.findall(r'123', ss))  # re.findall -> list타입으로 찾아서 반환

# 같은 결과
print()
print(re.findall(r'[0-9]', ss)) 
print(re.findall(r'\d', ss)) 

print()
print(re.findall(r'[0-9]+', ss))  # + -> 1회 이상 나오는 것들 묶기 
print(re.findall(r'[0-9]{2}', ss))
print(re.findall(r'\d{2}', ss))
print(re.findall(r'[0-9]{2,3}', ss)) 

print('====' * 10)
print(re.findall(r'.bc', ss))  # . -> 어떤 문자가 오든
print(re.findall(r'^1+', ss))  # ^ -> 해당 위치 글자가 1 ( 첫글자가 1 ) 
print(re.findall(r'[^1]+', ss))  # [ ] 범위 안에 들어오면 부정. 첫 글자가 1이 아님
print(re.findall(r'[^0-9]+', ss))  # 첫글자가 숫자가 아님
print(re.findall(r'nbc$', ss))

a= re.findall(r'123', ss)
print(a)
print(a.group())