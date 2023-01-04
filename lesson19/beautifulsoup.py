import requests
from bs4 import BeautifulSoup

URL = "https://www.franksonnenbergonline.com/blog/are-you-grateful/"

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'lxml')

print("Парсим заголовки")
for h in soup.find_all(['h1', 'h3']):
    print(h)

print("Парсим теги span, с указаным цветом")
# style="color: #ff6600;"
spans = soup.find_all('span', {"style": "color: #ff6600;"})
for span in spans:
    print(span)

print(spans[0].strong)

# <li id="menu-item-9624"></li>
li_item = soup.find('li', {"id": "menu-item-9624"})
print(li_item)

sister = li_item.next_sibling
print(sister)  # /n
print(sister.next_sibling)  # следующий li

print(sister.parent.parent.parent) #  Переходы к родительским элементам

# Найтёт первый элемент с тегом h1
print(soup.select("h1"))
print(soup.select_one("ul li"))


# Медленный, но знакомый способ
response = requests.get("https://content2.onliner.by/catalog/device/header/f298c4b10be5b4c756de1ab0e050fdd1.jpeg")
with open("file_name.jpeg", "wb") as image:
    image.write(response.content)

# import httplib2
#
# h = httplib2.Http('.cache')
# response, content = h.request(img)
# out = open('...\img.jpg', 'wb')
# out.write(content)
# out.close()
