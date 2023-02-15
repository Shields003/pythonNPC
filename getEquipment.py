import requests
import random
import getCharacterLevel

level = getCharacterLevel.character_level

urlEquipment = "https://www.dnd5eapi.co/api/equipment"
response = requests.get(urlEquipment)
data = response.json()
equipment = data["results"]

class getEquipment:
    def __init__(self):
        self.equipmentList = []
        self.equipment = equipment
        
    def addEquipment(self):
        selected_equipment = random.choice(self.equipment)
        self.equipmentList.append(selected_equipment["name"])
        
    def printEquipment(self):
        return [name for name in self.equipmentList[:10]]

inventory = getEquipment()

for i in range(level):
    inventory.addEquipment()

equipment_string = ", ".join(inventory.printEquipment())
