import requests
import random

urlSkills = "https://www.dnd5eapi.co/api/proficiencies"
response = requests.get(urlSkills)
data = response.json()
skill = data["results"]

class getSkills:
    def __init__(self):
        self.skillList = []
        self.skill = skill
        
    def addSkill(self):
        selected_skill = random.choice(self.skill)
        self.skillList.append(selected_skill["name"])
        
    def printSkill(self):
        return [name for name in self.skillList[:10]]

inventory = getSkills()
inventory.addSkill()
inventory.addSkill()
inventory.addSkill()
inventory.addSkill()
inventory.addSkill()
inventory.addSkill()
inventory.addSkill()
inventory.addSkill()
inventory.addSkill()


skill_string = ", ".join(inventory.printSkill())