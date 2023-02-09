import requests
import random

urlEquipment = "https://www.dnd5eapi.co/api/equipment"
response = requests.get(urlEquipment)
data = response.json()
equipment = data["results"]
equipmentList = []

selected_equipment1 = random.choice(equipment)
selected_equipment2 = random.choice(equipment)
selected_equipment3 = random.choice(equipment)
selected_equipment4 = random.choice(equipment)
selected_equipment5 = random.choice(equipment)
selected_equipment6 = random.choice(equipment)
selected_equipment7 = random.choice(equipment)
selected_equipment8 = random.choice(equipment)
selected_equipment9 = random.choice(equipment)
selected_equipment10 = random.choice(equipment)
#Make the previous 10 lines into a function that takes a number as an argument and returns a list of that many random equipment items.

equipmentList.append(selected_equipment1["name"])
equipmentList.append(selected_equipment2["name"])
equipmentList.append(selected_equipment3["name"])
equipmentList.append(selected_equipment4["name"])
equipmentList.append(selected_equipment5["name"])
equipmentList.append(selected_equipment6["name"])
equipmentList.append(selected_equipment7["name"])
equipmentList.append(selected_equipment8["name"])
equipmentList.append(selected_equipment9["name"])
equipmentList.append(selected_equipment10["name"])

equipmentNames = [name for name in equipmentList]

def printEquipment():
     for equipment in equipmentNames:
         print(equipment)
     if len(equipmentNames) == 0:
         print("No skills selected")
     elif equipment == "None":
         print("No skills selected")
         
