import random
import requests

def generate_class():
    urlClasses = "https://www.dnd5eapi.co/api/classes"

    response = requests.get(urlClasses)

    if response.status_code == 200:
        data = response.json()
        classes = data["results"]
        selected_class = random.choice(classes)
        return selected_class
    else:
        print("Failed to retrieve data")
        return None

selected_class = generate_class()
