import random
import requests

def generate_race():
    urlRaces = "https://www.dnd5eapi.co/api/races"

    response = requests.get(urlRaces)

    if response.status_code == 200:
        data = response.json()
        races = data["results"]
        selected_race = random.choice(races)
        return selected_race["name"]
    else:
        print("Failed to retrieve data")
        return None

