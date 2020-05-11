# 우편번호 파일 읽기 : 동 이름 입력 후 해당 자료 출력

try:
    dong = input('동 이름 입력 : ')
    
    with open(r'zipcode.txt', mode='r', encoding='euc-kr') as ff1:
        line = ff1.readline()
        # print(line)
        while line:
            #print(line)
            #lines = ff1.readline()
            lines = line.split(chr(9))
            # print(lines[3])
            if lines[3].startswith(dong):
                #print(lines)
                print('['+ lines[0] + ']' + lines[1] + '\t' + lines[2] + '\t' + lines[3])
                
            line = ff1.readline() 
            
except Exception as err:
    print('err : ' + str(err))
    
