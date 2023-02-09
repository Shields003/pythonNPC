import requests
import random

randAlignment = random.randint(0, 8)

urlBackgrounds = "https://www.dnd5eapi.co/api/backgrounds"

response = requests.get(urlBackgrounds)
data = response.json()
background = data["results"]
selectedBackground = random.choice(background)