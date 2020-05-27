# file로 저장

import pandas as pd

items = {'apple':{'count':10, 'price':1500},
         'orange':{'count':5, 'price':1000}
         }
df = pd.DataFrame(items)
print(df)

# 저장 하기
# 
# df.to_csv('result1.csv', sep=',')
# # 색인 제외
# df.to_csv('result2.csv', sep=',', index=False)
# # 색인 / 헤더 제외
# df.to_csv('result3.csv', sep=',', index=False, header=False)

# T 하고 저장하기
data = df.T
print(data)
print()
data.to_csv('result4.csv', sep=',', index=False, header=True)
redata = pd.read_csv('result4.csv')
print(redata)

print("------------------------------------------------------")
# 예외처리 주는게 좋다.(try-except)
# 엑셀에는 sheet가 나뉘어 있어 좀 더 까다롭다.
df2 = pd.DataFrame({'data':[1, 2, 3, 4, 5]})
print(df2)

# 엑셀로 저장하기
#
# writer = pd.ExcelWriter('good.xlsx', engine='xlsxwriter')
# df2.to_excel(writer, sheet_name = "Sheet1")
# writer.save()
# print('저장 성공')

exf = pd.ExcelFile('good.xlsx')
print(exf.sheet_names)

# DataFrame 반환함
df3 = exf.parse("Sheet1")

print(df3, type(df3))
print()

# r : read / b : binary
df4 = pd.read_excel(open('good.xlsx', 'rb'))
# 시트 이름을 명시해주면 더 좋다.
df4 = pd.read_excel(open('good.xlsx', 'rb'), sheet_name='Sheet1')
print(df4)

