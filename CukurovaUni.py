import requests
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
