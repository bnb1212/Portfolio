'''===========================================================
미국, 일본, 중국 사람들의 한국 관광지 선호 지역 상관관계 분석
==========================================================='''
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False


def setScatterCorr(tour_table, all_table, tourpoint):
    # 계산할 관광지 명에 해당하는 데이터만 뽑아 tour에 저장하고, 외국인 관광객 자료와 병합
    # tourpoint 순서대로 처리
    tour = tour_table[tour_table['resNm'] == tourpoint]
    print(tour.head(5))
    # merge
    print(all_table.head(3))
    merge_table = pd.merge(tour, all_table, left_index=True, right_index=True)
    print(merge_table)
    
    
    # 중국인 시각화 ----------------
    plt.subplot(1, 3, 1)
    plt.xlabel('중국인 입장수')
    plt.ylabel('외국인 입장수')
    
    # 상관계수 r 얻기
    lamb1 = lambda p:merge_table['china'].corr(merge_table['ForNum'])
    r1 = lamb1(merge_table)
    
    plt.title('r:{:.5f}'.format(r1))
    plt.scatter(merge_table['china'], merge_table['ForNum'], s=6, c='black')
#     plt.show()
    
    # 일본인 시각화--------------
    plt.subplot(1, 3, 2)
    plt.xlabel('일본인 입장수')
    plt.ylabel('외국인 입장수')
    
    # 상관계수 r 얻기
    lamb2 = lambda p:merge_table['japan'].corr(merge_table['ForNum'])
    r2 = lamb2(merge_table)
    
    plt.title('r:{:.5f}'.format(r2))
    plt.scatter(merge_table['japan'], merge_table['ForNum'], s=6, c='red')
    
    # 미국인 시각화 -----------
    plt.subplot(1, 3, 3)
    plt.xlabel('미국인 입장수')
    plt.ylabel('외국인 입장수')
    
    # 상관계수 r 얻기
    lamb3 = lambda p:merge_table['usa'].corr(merge_table['ForNum'])
    r3 = lamb3(merge_table)
    
    plt.title('r:{:.5f}'.format(r3))
    plt.scatter(merge_table['usa'], merge_table['ForNum'], s=6, c='blue')
    
    
    plt.tight_layout() 
    plt.show()
    
    return [tourpoint, r1, r2, r3]
    
# 실행 함수
def Gogo():
    fname = '서울특별시_관광지입장정보_2011_2016.json'
    jsonTp = json.load(open(fname, 'r', encoding='utf-8'))
    
    print(jsonTp, type(jsonTp))  # <class 'list'>
    tour_table = pd.DataFrame(jsonTp, columns=('yyyymm', 'resNm', 'ForNum'))  # 년월일, 관광지명, 입장객수
    tour_table= tour_table.set_index('yyyymm')
    print(tour_table.head())
    
    # 관광지 이름 얻기
    resNm = tour_table.resNm.unique()
    print(resNm)
    print('대상 관광지 이름 : ', resNm[:5])
    
    # 중국인 관광객 정보
    cdf = '중국인방문객.json'
    jdata = json.loads(open(cdf, 'r', encoding='utf-8').read())
    print(jdata)
    china_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    # 컬럼명 rename (활용을 위해)
    china_table = china_table.rename(columns={'visit_cnt':'china'})
    china_table = china_table.set_index('yyyymm')
    print(china_table.head(3))
    
    # 일본인 관광객 정보
    jdf = '일본인방문객.json'
    jdata = json.loads(open(jdf, 'r', encoding='utf-8').read())
    print(jdata)
    japan_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    # 컬럼명 rename (활용을 위해)
    japan_table = japan_table.rename(columns={'visit_cnt':'japan'})
    japan_table = japan_table.set_index('yyyymm')
    print(japan_table.head(3))
    
    # 미국인 관광객 정보
    udf = '미국인방문객.json'
    jdata = json.loads(open(udf, 'r', encoding='utf-8').read())
    print(jdata)
    usa_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    # 컬럼명 rename (활용을 위해)
    usa_table = usa_table.rename(columns={'visit_cnt':'usa'})
    usa_table = usa_table.set_index('yyyymm')
    print(usa_table.head(3))
    
    # 병합(merge)
    all_table = pd.merge(china_table, japan_table, left_index=True, right_index=True)
    all_table = pd.merge(all_table, usa_table, left_index=True, right_index=True)
    print(all_table.head(3))
    
    # 각 관광지(5군데) 마다 상관계수를 구해 기억
    r_list = []
    for tourpoint in resNm[:5]:
#         print(tourpoint)
        # 시각화 + 상관계수 처리 함수 호출
        r_list.append(setScatterCorr(tour_table, all_table, tourpoint))
        
    # print(r_list)
    r_df = pd.DataFrame(r_list, columns = ('고궁명', '중국', '일본', '미국'))
    r_df = r_df.set_index('고궁명')
    
    print(r_df)
    
    r_df.plot(kind='bar', rot = 50)
    plt.show()
    
if __name__ == '__main__':
    Gogo()
    
