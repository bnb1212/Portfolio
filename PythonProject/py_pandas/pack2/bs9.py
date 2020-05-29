# 급상승 인기 검색어
import requests
from bs4 import BeautifulSoup

class GoNaver():
    def sijak(self):
        url = "https://datalab.naver.com/keyword/realtimeList.naver?age=all"
        # 접근 제한 메세지가 뜨면 headers를 넣어보자
        page = requests.get(url,
                            headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'})
        soup = BeautifulSoup(page.text, 'lxml')
        print(soup)
        title = soup.select('span.item_title')
        print(title)
        print('네이버 실시간 검색어')
        count = 0
        for i in title:
            count += 1
            print(str(count) + ") " + i.string)
            
            
if __name__ == '__main__':
    GoNaver().sijak()