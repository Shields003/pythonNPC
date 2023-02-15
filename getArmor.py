import random
import requests

url_armor = "https://www.dnd5eapi.co/api/equipment-categories/armor"

response = requests.get(url_armor)

if response.status_code == 200:
    data = response.json()
    armor = data["equipment"]
    selected_armor= random.choice(armor)
else:
    print("Failed to retrieve data")
    
# Get the armor class of the selected armor
# url_armor_class = ["https://www.dnd5eapi.co/api/equipment-categories/", selected_armor, "/", "armor-class", "/"]
# response2 = requests.get(url_armor_class)

# if response2.status_code == 200:
#     data = response2.json()
#     armor_class = data["armor_class"]

# if response.status_code == 200:
#     data = response.json()
#     armor_class = data["equipment"]
   
# ac = armor_class["armor_class"]

# ac = selected_armor["armor_class"]
