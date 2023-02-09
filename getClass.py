import random
import requests

urlClasses = "https://www.dnd5eapi.co/api/classes"

response = requests.get(urlClasses)

if response.status_code == 200:
    data = response.json()
    classes = data["results"]
    selected_class = random.choice(classes)
#     print(selected_class["name"])
else:
    print("Failed to retrieve data")
