import requests
from bs4 import BeautifulSoup

url = "https://www.erbakan.edu.tr/biyoteknoloji/anabilim"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

list= soup.find_all("div",{"class":"col-xs-12 col-sm-6 col-md-4 academic-person"})


for i in list:
    isim =i.find("div",{"class":"academic-person-name"}).find_all("span")

for a in list:
    mail=a.find("a",{"class":"academic-person-mail"}).find_all("href")
    print(mail)

print("-------------------------------------------")
print("-------------------------------------------")
print("-------------------------------------------")


isim = BeautifulSoup(html,"html.parser")
mail = BeautifulSoup(html,"html.parser")



for isim_tag in isim.find_all('span'):
    print(isim_tag.text)



""" for mail_tag in mail.find_all('href'):
    print(mail_tag.text) """
    



