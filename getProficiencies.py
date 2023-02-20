import requests
import getRace
import getClass

url_base = "https://www.dnd5eapi.co/api/classes/"
full_url = url_base + getClass.selected_class["index"]

response = requests.get(full_url)

proficiency_list = []
saving_throw_list = []

if response.status_code == 200:
    data = response.json()
    proficiencies = data["proficiencies"]
    for proficiency in proficiencies:
        proficiency_list.append(proficiency["name"])
else:
    print("Failed to retrieve data")

for item in proficiency_list[:]:
    if item.startswith("Saving"):
        proficiency_list.remove(item)
        saving_throw_list.append(item)

proficiency_string = ", ".join(proficiency_list)
saving_throw_string = ", ".join(saving_throw_list)

print(saving_throw_list)
print(proficiency_list)