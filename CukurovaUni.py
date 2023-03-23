import requests
from bs4 import BeautifulSoup

url = "https://bmb.cu.edu.tr/cu/personel/akademik-personel"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

list = soup.find_all("div",{"class":"blog-post__content"})

#mail finding
for i in list:
    tbody = i.find("tbody")
    for td in tbody.find_all("td"):
        if "@" in td.text:
            mailler=print(td.text)

print("----------------------")

for i in list:
    tbody = i.find("tbody")
    for td in tbody.find_all("td"):
        if "@" in td.text:
            pass
        else:
            isimler= print(td.text)


print(f"isim:{isimler} mail:{mailler}")
