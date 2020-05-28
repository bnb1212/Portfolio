# 입력
test_cases = int(input())
case = []
for c in range(test_cases):
    case.append(list(map(int, input().split())))

# 출력
# 평균을 구하자

case_avg_list = []
for c in range(test_cases):
    case_avg_list.append((sum(case[c]) - case[c][0]) / case[c][0])
# print(case_avg_list)

for c in range(len(case)):
    count = 0
    # c의 리스트 반복. c[0]은 학생의 수.
#     print(case[c][0])
    for s in range(1, case[c][0] + 1):
        if case[c][s] > case_avg_list[c]:
            count += 1
    print("{0:.3%}".format(count / case[c][0]))
