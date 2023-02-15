import random
import requests

urlWeapons = "https://www.dnd5eapi.co/api/equipment-categories/weapon"

response = requests.get(urlWeapons)

if response.status_code == 200:
    data = response.json()
    weapons = data["equipment"]
    selected_weapon = random.choice(weapons)

    selected_weapon2 = random.choice(weapons)
else:
    print("Failed to retrieve data")
    
    
# If the selected weapons name contains "Weapon" then it will select another weapon.
if "Weapon" in selected_weapon["name"]:
    selected_weapon = random.choice(weapons)

if "Weapon" in selected_weapon2["name"]:
    selected_weapon2 = random.choice(weapons)