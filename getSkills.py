import requests
import random
import getCharacterLevel
import getProficiencies

urlSkills = "https://www.dnd5eapi.co/api/proficiencies"
response = requests.get(urlSkills)
data = response.json()
skill = data["results"]

class getSkills:
    def __init__(self):
        self.skillList = []
        self.saving_skillList = []
        self.skill = skill
        
    def addSkill(self):
        selected_skill = random.choice(self.skill)
        if selected_skill["name"].startswith("Saving"):
            self.saving_skillList.append(selected_skill["name"])
        if selected_skill["name"].startswith("Skill"):
            self.skillList.append(selected_skill["name"])
        else:
            self.skillList.append(selected_skill["name"])
        
    def printSkill(self):
        return [name for name in self.skillList[:10]]

inventory = getSkills()

# This adds a skill to the inventory list for every level of the character

for i in range(getCharacterLevel.character_level):
    inventory.addSkill()

# getSkills()

skill_string = ", ".join(inventory.printSkill())
saving_throws = inventory.saving_skillList

proficiency_list = getProficiencies.proficiency_list


# print("-------------------------------")
# print("-------------------------------")
# print("Proficiencies:  ", skill_string)
# print("Saving Throws:  ", saving_throws)
# print("-------------------------------")
# print("-------------------------------")



# # This code will build a list of the optional skills.

# skills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]