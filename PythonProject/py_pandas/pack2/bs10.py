# 구글 검색 기능을 이용해 검색 결과(a tag)의 갯수 만큼
import requests
from bs4 import BeautifulSoup
import webbrowser

def searchFunc():
    base_url= "https://www.google.com/search?q={0}"
    s_word = base_url.format('파이썬')
    print(s_word) # https://www.google.com/search?q=파이썬
    
    plain_text = requests.get(s_word, 
                            headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'})
#     print(plain_text)
    
    soup = BeautifulSoup(plain_text.text, 'lxml')
#     print(soup)
    # link_data = soup.select('a')
    link_data = soup.select('div > div.r > a')
    print(link_data)
    
    print()
    for link in link_data[:3]:
        #print(link)
        print(type(link), type(str(link)))
        print(str(link).find('https'), ' ', str(link).find('onmousedown') -2)
        urls = str(link)[str(link).find('https'):str(link).find('onmousedown') -2]
        print(urls)
        
        webbrowser.open(urls) # 브라우저로 출력
        
    
searchFunc()