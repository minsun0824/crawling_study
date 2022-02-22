import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday"
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) #soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs) # a element의 속성정보를 출력
# print(soup.a["href"]) # a element의 href 속성 값 정보를 출력

# print(soup.find("a",attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인  a element를 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"}))
# #class="Nbtn_upload" 인 어떤 element를 찾아줘

# #print(soup.find("li",attrs={"class":"rank01"}))
#rank1=soup.find("li",attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2=rank1.next_sibling.next_sibling
# print(rank2.a.get_text())

#next sibling 두 번 하는거 번거로운 경우
# rank2=rank1.find_next_sibling("li") #이전 형제는 find_previous sibling
# print(rank2.a.get_text())

#형제 여러개 가져오기
#print(rank1.find_next_siblings("li"))

webtoon=soup.find("a",text="싸움독학-110화 : 술자리 예절!")
print(webtoon)
