import requests
from bs4 import BeautifulSoup

url = "https://bmb.cu.edu.tr/cu/personel/akademik-personel"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

list = soup.find_all("div",{"class":"blog-post__content"})


names = []
emails = []



rows = soup.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    if len(cols) >= 2:
        first_col = cols[0].get_text().strip()
        second_col = cols[1].get_text().strip()
        print(first_col, second_col)

print("----------------------")
        
with open('output.txt', 'w') as f:
    for row in rows:
        cols = row.find_all('td')
        first_col = cols[0].get_text().strip()
        second_col = cols[1].get_text().strip()
        f.write(first_col + '\t' + second_col + '\n')
    

print("----------------------")


#mail finding
for i in list:
    tbody = i.find("tbody")
    for td in tbody.find_all("td"):
        if "@" in td.text:
            mailler=print(td.text)
            emails.append(td.text)

print("----------------------")

