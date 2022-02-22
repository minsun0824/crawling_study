import requests
from bs4 import BeautifulSoup





def scrape_weather():
    print("[오늘의 날씨]")
    url="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"lxml")

if __name__=="__main__":
    scrape_weather()