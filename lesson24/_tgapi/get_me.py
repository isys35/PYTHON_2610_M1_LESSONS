
import requests

from lesson24._tgapi.config import TOKEN


url = f"https://api.telegram.org/bot{TOKEN}/"


# response = requests.get(url + "getMe")
# response.raise_for_status()
# print(response.json())


response = requests.get(url + "getUpdates")
response.raise_for_status()

updates = response.json()
for update in updates["result"]:
    chat_id = update["message"]["chat"]["id"]
    requests.post(url + "sendMessage", data={"chat_id": chat_id, "text": "Здарова!"})
print(response.json())


