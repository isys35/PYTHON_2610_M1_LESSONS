import requests
from requests import HTTPError
import json
from getpass import getpass

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}


def save_html(file_name, content):
    with open(file_name, "wb") as html_file:
        html_file.write(content)


def get_google_page():
    response = requests.get("https://www.youtube.com/")
    response.raise_for_status()
    with open("youtube.html", "wb") as html_file:
        # response.text Для получения текста
        # response.json() Для получения словаря
        html_file.write(response.content)


def parse_computers():
    MAIN_URL = "https://www.wildberries.by/catalog/elektronika/noutbuki-periferiya/kompyutery"
    # sort=popular&page=2&cardSize=c516x688&xsubject=2875&bid=2a9a1e9b-0e5a-4443-a596-35da02723182
    params = {"sort": "popular", "page": 2, "cardSize": "c516x6880", "xsubject": "2875",
              "bid": "2a9a1e9b-0e5a-4443-a596-35da02723182"}
    response = requests.get(MAIN_URL, params=params, headers=HEADERS)
    response.raise_for_status()
    save_html("computers_page_2.html", response.content)
    # print(response.request.url)


def parse_menu():
    URL = "https://static-basket-01.wb.ru/vol0/data/main-menu-by-ru.json"
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()
    print(response.json())


def parse_computers_v2():
    url = "https://catalog.wb.ru/catalog/electronic15/catalog?__tmp=by&appType=1&couponsGeo=12,7,3,21&curr=byn&dest=12358386,12358403,-70563,-8139704&emp=0&lang=ru&locale=by&page=2&pricemarginCoeff=1&reg=0&regions=80,83,4,33,70,69,86,30,40,48,1,66,31,68,22&sort=popular&spp=0&subject=2872;2875&xsubject=2875"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    with open("computers_page_2.json", "w") as json_file:
        json.dump(response.json(), json_file, indent=4)
    print(response.headers)
    # for item in response.json()["data"]["products"]:
    #     print(item["name"], item["brand"], item['salePriceU']/100, item['priceU']/100)


def get_me_github():
    response = requests.get('https://api.github.com/user', auth=('isys35', getpass()))
    response.raise_for_status()
    print(response.json())

if __name__ == '__main__':
    # try:
    #     get_google_page()
    # except HTTPError:
    #     print("Ошибка")

    # response = requests.post('https://httpbin.org/post', data={'key': 'value'})
    # response_2 = requests.post('https://httpbin.org/post', json="{'key': 'value'}")
    # parse_computers()
    # print(response_2.status_code)
    # parse_menu()
    # parse_computers_v2()
    get_me_github()