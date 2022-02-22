# import requests
# from bs4 import BeautifulSoup

# url="https://play.google.com/store/movies/collection/cluster?clp=6gIkIiIKHHByb21vdGlvbl9tb3ZpZXNfbmV3X3JlbGVhc2UQPxgE:S:ANO1ljIv2Z0&gsr=CifqAiQiIgoccHJvbW90aW9uX21vdmllc19uZXdfcmVsZWFzZRA_GAQ%3D:S:ANO1ljJ_5l0&hl=ko&gl=US"
# res=requests.get(url)
# res.raise_for_status()

# soup=BeautifulSoup(res.text,"lxml")

# movies =soup.find_all("div",attrs={"class":"ImZGtf mpg5gc"})
# print(len(movies))

# # with open("movie.html","w",encoding="utf8") as f:
# #     f.write(soup.prettify())

# for movie in movies:
#     title=movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
#     print(title)

from selenium import webdriver
browser=webdriver.Chrome()
browser.maximize_window()

url="https://play.google.com/store/movies/collection/cluster?clp=6gIkIiIKHHByb21vdGlvbl9tb3ZpZXNfbmV3X3JlbGVhc2UQPxgE:S:ANO1ljIv2Z0&gsr=CifqAiQiIgoccHJvbW90aW9uX21vdmllc19uZXdfcmVsZWFzZRA_GAQ%3D:S:ANO1ljJ_5l0&hl=ko&gl=US"
browser.get(url)

#browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

import time
interval=2

prev_height=browser.execute_script("return document.body.scrollHeight")

#반복 수행
while True:
    #스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    #페이지 로딩 대기
    time.sleep(interval)

    #현재 문서 높이를 가져와서 저장
    curr_height=browser.execute_script("return document.body.scrollHeight")
    if curr_height==prev_height:
        break
    prev_height=curr_height

print("스크롤 완료")

import requests
from bs4 import BeautifulSoup

soup=BeautifulSoup(browser.page_source,"lxml")

movies =soup.find_all("div",attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))


for movie in movies:
    title=movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)