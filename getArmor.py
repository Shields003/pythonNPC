import random
import requests
import getStats

response = requests.get(
    "https://www.dnd5eapi.co/api/equipment-categories/armor")

if response.status_code == 200:
    armor_list = response.json()["equipment"]
    random_armor = random.choice(armor_list)
    armor_name = random_armor["name"]
else:
    print("Failed to retrieve data")

ARMOR_CLASSES = {
    "Padded": 11,
    "Leather": 11,
    "Studded Leather": 12,
    "Hide": 12,
    "Chain Shirt": 13,
    "Scale Mail": 14,
    "Breastplate": 14,
    "Half Plate": 15,
    "Ring Mail": 14,
    "Chain Mail": 16,
    "Splint": 17,
    "Plate": 18,
}


def get_armor():
    response = requests.get(
        "https://www.dnd5eapi.co/api/equipment-categories/armor")

    if response.status_code != 200:
        raise Exception("Failed to retrieve data")

    armor_list = response.json()["equipment"]
    random_armor = random.choice(armor_list)
    armor_name = random_armor["name"]
    armor_class = ARMOR_CLASSES.get(armor_name, 10)

    return armor_name, armor_class

