# 기상청 날씨 정보 xml 자료 읽기
import xml.etree.ElementTree as etree
from urllib.request import urlopen
import pandas

# try:
#     webdata = urlopen('http://www.kma.go.kr/XML/weather/sfc_web_map.xml')
#     webxml = webdata.read()
# #     print(webxml)
#     webxml = webxml.decode('utf-8')
#     print(webxml)
#     webdata.close()
#     
#     with open('myweather.xml', mode='w', encoding='utf-8') as f:
#         f.write(webxml)
#     
# except Exception as e:
#     print("Error :", e)
#     
xmlfile = etree.parse('myweather.xml')
print(xmlfile)
root = xmlfile.getroot()
print(root.tag)
print(root[0].tag)
child = root.findall('{current}weather')
child = root.findall(root[0].tag)
print(child)

for i in child:
    y = i.get('year')
    m = i.get('month')
    d = i.get('day')
    h = i.get('hour')
    print(y + "년" + m + "월" + d + "일" + h + "시 현재")

datas = []
for ch in root:
    for i in ch:
#         print(i.tag) # {current} local
        localName = i.text
        print(localName)
        ta = i.get('ta')
        desc = i.get('desc')
        datas += [[localName, ta, desc]]
        
from pandas import DataFrame
# print(datas)

df = pandas.DataFrame(datas)
# 머리 5개
print(df.head())
print()
# 꼬리 3개
print(df.tail(3))

print()
print('웹 자료 읽어 바로 출력')
import urllib.request

webdata2 = urllib.request.urlopen('http://www.kma.go.kr/XML/weather/sfc_web_map.xml')
xmlFile =etree.parse(webdata2) 
root = xmlFile.getroot()
ndate = list(root[0].attrib.values())
# print(ndate)
print(ndate[0] + '년' + ndate[1] + '월' + ndate[2] + '일' +ndate[3] + "시")

for child in root:
    for subChild in child:
        print(subChild.text + " : " + subChild.attrib.get("ta"))


# 웹 이미지
imgUrl = "https://post-phinf.pstatic.net/MjAxOTA4MzBfMjY1/MDAxNTY3MTQ5ODUyMjIz.WR3eIHPD4mcmcOptMtE0aIXFexAsKhZvTb9Ahs77ff8g.s050HZxtAJ08n5P4UHf8lYj01MYESkrhTHxA8Qz9mHMg.JPEG/04a.jpg?type=w1200"
saveName = "myimage.png"
urllib.request.urlretrieve(imgUrl, saveName)
