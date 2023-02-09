import requests
import random

randAlignment = random.randint(0, 8)

urlAlignments = "https://www.dnd5eapi.co/api/alignments"

response = requests.get(urlAlignments)
data = response.json()
alignment = data["results"]
selectedAlignment = random.choice(alignment)