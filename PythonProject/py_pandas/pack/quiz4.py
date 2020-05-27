import pandas as pd

print("------------------- Quiz 4 ------------------------------")
# 각 컬럼명 / values에 공백이 있음
# df2 = pd.read_csv('../testdata/human.csv', na_values=' NA')
# df2.rename(columns=lambda x: x.strip())
# print(df2)
try:
    print('-------- NA 삭제 ------')
    df2 = pd.read_csv('../testdata/human.csv', skipinitialspace=True)
    print(df2)
    print(df2.dropna())
    print()
    print('-------- 칼럼 추출하여 DF 작성 ------')
    p_df2 = df2.loc[:,['Career', 'Score']]
    print(p_df2)
    print("Career 평균 :",p_df2['Career'].mean())
    print("Score 평균 :",p_df2['Score'].mean())
except Exception as e:
    print("Error : " + str(e))
    
