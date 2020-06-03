import pandas as pd
from pandas_datareader import data


# 종목 읽기
kosdaq = pd.read_pickle('./kosdaq.pickle') 
kospi = pd.read_pickle('./kospi.pickle')

print(kosdaq.head(3))
print(kospi.head())
 
# Yahoo에서 읽기
start_date = '2018-01-01'
tickers=['003380.KQ', '251270.KS'] # 제일 홀딩스, 넷마블 게임즈
holding_df = data.get_data_yahoo(tickers[0], start_date)
print(holding_df.head(3))
print()
net_df = data.get_data_yahoo(tickers[1], start_date)
print(net_df.head(3))
 
# file로 저장
# holding_df.to_csv('./holding.csv')
# net_df.to_csv('./net.csv')
#  
# holding_df.to_pickle('./holding.pickle')
# net_df.to_excel('./net.xlsx')
 
# with open('./holding.csv', mode='r') as f:
#     print(f.read())
     
     
print()

# 시각화
import matplotlib.pyplot as plt
# plt.plot(holding_df)
# plt.show()
# 
# plt.plot(net_df)
# plt.show()
print()

import numpy as np
# pandas가 plot 기능
np.random.seed(0)

df = pd.DataFrame(np.random.randn(10, 3),
                  # date_range메소드
                  index=pd.date_range('1/1/2000', periods=10),
                  columns=['a','b','c'])
print(df)

    # df.plot()
    # df.plot(kind='bar') # 'box' ...
df[:5].plot.bar(rot = 15)
plt.title('test')

plt.show()