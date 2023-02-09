import requests
import random

urlSkills = "https://www.dnd5eapi.co/api/proficiencies"
response = requests.get(urlSkills)
data = response.json()
skill = data["results"]

selected_skill1 = random.choice(skill)
selected_skill2 = random.choice(skill)
selected_skill3 = random.choice(skill)
selected_skill4 = random.choice(skill)
selected_skill5 = random.choice(skill)
selected_skill6 = random.choice(skill)
selected_skill7 = random.choice(skill)
selected_skill8 = random.choice(skill)
selected_skill9 = random.choice(skill)
selected_skill10 = random.choice(skill)
level = random.randint(1, 20)
skillList = [""]
skillList.append(selected_skill1["name"])
skillList.append(selected_skill2["name"])
skillList.append(selected_skill3["name"])
skillList.append(selected_skill4["name"])
skillList.append(selected_skill5["name"])
skillNames = [name for name in skillList]


def printSkills():
    for skill in skillNames:
        print(skill)
        
printSkills()
