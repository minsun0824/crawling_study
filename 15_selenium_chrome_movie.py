import requests
from bs4 import BeautifulSoup

url="https://play.google.com/store/movies/collection/cluster?clp=6gIkIiIKHHByb21vdGlvbl9tb3ZpZXNfbmV3X3JlbGVhc2UQPxgE:S:ANO1ljIv2Z0&gsr=CifqAiQiIgoccHJvbW90aW9uX21vdmllc19uZXdfcmVsZWFzZRA_GAQ%3D:S:ANO1ljJ_5l0&hl=ko&gl=US"
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")

movies =soup.find_all("div",attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

# with open("movie.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())

for movie in movies:
    title=movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)