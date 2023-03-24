import requestsimport requests
from bs4 import BeautifulSoup

url = "https://www.erbakan.edu.tr/biyoteknoloji/anabilim"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

list= soup.find_all("div",{"class":"col-xs-12 col-sm-6 col-md-4 academic-person"})


for i in list:
    isim =i.find("div",{"class":"academic-person-name"}).find_all("span")

for a in list:
    mail=a.find("a",{"class":"academic-person-mail"},href=True)
    emails=print(mail["href"])

print("-------------------------------------------")
print("-------------------------------------------")
print("-------------------------------------------")


isim = BeautifulSoup(html,"html.parser")
mail = BeautifulSoup(html,"html.parser")



for isim_tag in isim.find_all('span'):
    print(isim_tag.text)



""" for mail_tag in mail.find_all('href'):
    print(mail_tag.text) """


print("-------------------------------------------")
print("-------------------------------------------")
print("-------------------------------------------")
    

""" def decodeEmail(e):
    de = ""
    k = int(e[:2], 16)

    for i in range(2, len(e)-1, 2):
        de += chr(int(e[i:i+2], 16)^k)

    return de

de_emails = decodeEmail(emails)
print(de_emails) """

from bs4 import BeautifulSoup

url = "https://bmb.cu.edu.tr/cu/personel/akademik-personel"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")
import requests
from bs4 import BeautifulSoup

url = "https://bmb.cu.edu.tr/cu/personel/akademik-personel"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

list = soup.find_all("div",{"class":"blog-post__content"})


names = []
emails = []



for row in list:
    cells = row.find_all('td')
    for cell in cells:
        first_td = cells[0].get_text()
        second_td = cells[1].get_text()
        print(cell.text)

print("----------------------")
        
    
    

print("----------------------")


#mail finding
for i in list:
    tbody = i.find("tbody")
    for td in tbody.find_all("td"):
        if "@" in td.text:
            mailler=print(td.text)
            emails.append(td.text)

print("----------------------")

for i in list:
    tbody = i.find("tbody")
    for td in tbody.find_all("td"):
        if "@" in td.text:
            pass
        else:
            isimler= print(td.text)
            names.append(td.text)
            

print("----------------------")

with open('names_emails.txt', 'w') as file:
    for name, email in zip(names, emails):
        file.write(name + ' =' + email + '\n')


for name, email in zip(names, emails):
    print(name + '=' + email)


list = soup.find_all("div",{"class":"blog-post__content"})

#mail finding
for i in list:
    tbody = i.find("tbody")
    for td in tbody.find_all("td"):
        if "@" in td.text:import requests
from bs4 import BeautifulSoup

url = "https://bmb.cu.edu.tr/cu/personel/akademik-personel"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

list = soup.find_all("div",{"class":"blog-post__content"})


names = []
emails = []



for row in list:
    cells = row.find_all('td')
    for cell in cells:
        first_td = cells[0].get_text()
        second_td = cells[1].get_text()
        print(cell.text)

print("----------------------")
        
    
    

print("----------------------")


#mail finding
for i in list:
    tbody = i.find("tbody")
    for td in tbody.find_all("td"):
        if "@" in td.text:
            mailler=print(td.text)
            emails.append(td.text)

print("----------------------")

for i in list:
    tbody = i.find("tbody")
    for td in tbody.find_all("td"):
        if "@" in td.text:
            pass
        else:
            isimler= print(td.text)
            names.append(td.text)
            

print("----------------------")

with open('names_emails.txt', 'w') as file:
    for name, email in zip(names, emails):
        file.write(name + ' =' + email + '\n')


for name, email in zip(names, emails):
    print(name + '=' + email)


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
