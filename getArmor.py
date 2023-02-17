import random
import requests

response = requests.get(
    "https://www.dnd5eapi.co/api/equipment-categories/armor")

if response.status_code == 200:
    armor_list = response.json()["equipment"]
    random_armor = random.choice(armor_list)
    armor_name = random_armor["name"]
else:
    print("Failed to retrieve data")

ac = 0

if armor_name == "Padded":
    ac = 11
elif armor_name == "Leather":
    ac = 11
elif armor_name == "Studded Leather":
     ac = 12
elif armor_name == "Hide":
     ac = 12
elif armor_name == "Chain Shirt":
     ac = 13
elif armor_name == "Scale Mail":
     ac = 14
elif armor_name == "Breastplate":
     ac = 14
elif armor_name == "Half Plate":
     ac = 15
elif armor_name == "Ring Mail":
     ac = 14
elif armor_name == "Chain Mail":
     ac = 16
elif armor_name == "Splint":
     ac = 17
elif armor_name == "Plate":
     ac = 18
else:
    ac = 10

# print(random_armor["index"])
# print(random_armor["name"])
