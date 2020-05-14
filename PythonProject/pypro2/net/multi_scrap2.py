# 멀티 프로세싱을 통한 웹 스크래핑 1 : multiprocessing X
import requests
from bs4 import BeautifulSoup as bs
import time
from conda.core import link

def get_link():
    url = "https://beomi.github.io/beomi.github.io_old/"
    html = requests.get(url).text
    
    # print(html)
    soup = bs(html, 'html.parser')
    # print(soup)
    
    # 페이지 내의 링크 긁어오기 ========================= 
    my_title = soup.select('h3 > a')
    data = []
    
    for title in my_title:
        data.append(title.get('href'))
        
    return data

    # 페이지 제목 (h1) 가져오기
def get_content(link):
    abc_link = 'https://beomi.github.io' + link
    data = requests.get(abc_link).text
    soup = bs(data, 'html.parser')
    print(soup.select('h1')[0].text)
    
    
if __name__ == '__main__':
    start_time = time.time()
#    print(get_link())
    for link in get_link():
        get_content(link)
        
    print("처리 시간 : %s 초"%(time.time() - start_time))
    
    

