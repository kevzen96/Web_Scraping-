import requests
from bs4 import BeautifulSoup
import pandas as pd

# ดึงข้อมูล
url = "https://notebookspec.com/topchart/notebook.html"
res = requests.get(url)

# สกัดข้อมูล
soup = BeautifulSoup(res.text, "html.parser")
notebook = soup.find('ul', class_="top-100-list").find_all('li')

rankls = []
namels = []
pricels = []

for i in notebook:
    rank = i.find("div", class_="num").text
    name = i.find('a').text.strip()
    price = i.find('div', class_="price").text
    rankls.append(rank)
    namels.append(name)
    pricels.append(price)

# เก็บข้อมูล
df = pd.DataFrame({'อันดับ':rankls, 'รายชื่อ':namels, 'ราคาสินค้า':pricels})
df.to_excel('Topnotebook.xlsx')