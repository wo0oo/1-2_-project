import requests
from bs4 import BeautifulSoup

url="https://lost112.go.kr/lost/lostList.do"
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")


items = soup.find_all("td", attrs={"class":"board_title1"})


for item in items:
    title=item.a.get_text()
    link=item.a["href"]
    print(title,link)
   