import requests
from bs4 import BeautifulSoup

url = "https://cash-backer.club/shops"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
headers = {"user-agent": user_agent}
session = requests.Session()

response = session.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")


    shops = soup.find_all("div", class_="cb-shop-item")

    with open("cashback_data.txt", "a", encoding="utf-8") as file:
        for shop in shops:

            shop_name = shop.find("h3", class_="cb-shop-title").text.strip()
            cashback_percentage = shop.find("div", class_="cb-shop-cashback").text.strip()


            file.write(f"Магазин: {shop_name}, Кешбек: {cashback_percentage}\n")


    pagination_links = soup.find_all("a", class_="cb-pagination-link")
    for link in pagination_links:
        page_url = link["href"]
        response = session.get(page_url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            shops = soup.find_all("div", class_="cb-shop-item")

            for shop in shops:
                shop_name = shop.find("h3", class_="cb-shop-title").text.strip()
                cashback_percentage = shop.find("div", class_="cb-shop-cashback").text.strip()
                file.write(f"Магазин: {shop_name}, Кешбек: {cashback_percentage}\n")
else:
    print(f"Не удалось получить страницу. Код состояния: {response.status_code}")
