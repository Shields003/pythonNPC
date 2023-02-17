import requests
import getRace
import getClass

url_base = "https://www.dnd5eapi.co/api/classes/"
full_url = url_base + getClass.selected_class["index"]

response = requests.get(full_url)

proficiency_list = []

if response.status_code == 200:
    data = response.json()
    proficiencies = data["proficiencies"]
    for proficiency in proficiencies:
        proficiency_list.append(proficiency["name"])
else:
    print("Failed to retrieve data")

proficiency_string = ", ".join(proficiency_list)




# if getClass.classes == "Bard":
#      proficiencies_URL = (getClass.selected_class["proficiencies_url"])
# elif getClass.classes == "Cleric":
#      proficiencies = (getClass.selected_class["proficiencies"])
# else:
#      print("No proficiencies")