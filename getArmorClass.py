import random
import requests

response = requests.get("https://www.dnd5eapi.co/api/equipment-categories/armor")

armor_list = response.json()["equipment"]
random_armor = random.choice(armor_list)

armor_name = random_armor["name"]

# print(random_armor["index"])
# print(random_armor["name"])

