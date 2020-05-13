# 멀티 프로세싱을 통한 웹 스크래핑 1 : multiprocessing X
import requests
from bs4 import BeautifulSoup as bs
import time

def get_link():
    req = requests.get("https://beomi.github.io/beomi.github.io_old/")
    html = req.text
    print(html)
    
    soup = bs(html, 'html.parser')
    
get_link()