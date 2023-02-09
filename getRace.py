import random
import requests

urlRaces = "https://www.dnd5eapi.co/api/races"

response = requests.get(urlRaces)

if response.status_code == 200:
    data = response.json()
    races = data["results"]
    selected_race = random.choice(races)
#     print(selected_class["name"])
else:
    print("Failed to retrieve data")
