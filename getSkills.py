import requests
import random
import getCharacterLevel

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

#This adds a skill to the inventory list for every level of the character

for i in range(getCharacterLevel.character_level):
    inventory.addSkill()


# inventory.addSkill()
# inventory.addSkill()
# inventory.addSkill()
# inventory.addSkill()
# inventory.addSkill()
# inventory.addSkill()
# inventory.addSkill()
# inventory.addSkill()
# inventory.addSkill()


skill_string = ", ".join(inventory.printSkill())

# # This code will build a list of the optional skills.

# skills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]