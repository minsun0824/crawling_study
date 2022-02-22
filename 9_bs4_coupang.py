import requests
import re
from bs4 import BeautifulSoup

url="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()
soup=BeautifulSoup(res.text,"html")

items=soup.find_all("li", attrs={"class":re.compile("^search-product")})
#print(items[0].find("div",attrs={"class":"name"}).get_text())


for item in items:
    name=item.find("div",attrs={"class":"name"}).get_text() #제품명
    #삼성 제품 제외
    if "삼성전자" in name:
        print(" <삼성 전자 제품 제외합니다>")
        continue
    price=item.find("strong",attrs={"class":"price-value"}).get_text() #가격
    rate=item.find("em",attrs={"class":"rating"})
    if rate:
        rate=rate.get_text()
    else:
        print(" <평점 없는 상품 제외합니다>")
        continue

    rate_num=item.find("span",attrs={"class":"rating-total-count"})
    
    if rate_num:
        rate_num=rate_num.get_text()
        rate_num=rate_num[1:-1]
        #print("리뷰 수",rate_num)
    else:
        print(" <평점 수 없는 상품 제외합니다>")
        continue

    if float(rate) >=4.5 and int(rate_num)>=100:
        print(name,price,rate,rate_num)
