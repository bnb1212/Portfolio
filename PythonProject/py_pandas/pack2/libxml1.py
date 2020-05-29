# 웹에서 제공되는 강남구 도서관 정보 XML 읽기
import urllib.request as req
from bs4 import BeautifulSoup

url = "http://openapi.seoul.go.kr:8088/sample/xml/SeoulLibraryTime/1/5/"
plain_text = req.urlopen(url).read().decode()
print(plain_text)

xmlObj = BeautifulSoup(plain_text, 'lxml')
libData = xmlObj.select('row')
print(libData)


for data in libData:
    name = data.find('lbrry_name').text
    addr = data.find('adres').text
    tel = data.find('tel_no').text
    print('도서관명 :', name)
    print('주소 :',name)
    print('전화 :',tel, '\n')

    

