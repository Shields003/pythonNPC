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

skillList = []

if level >= 1 and level <= 4:
   skillList.append(selected_skill1["name"])
   skillList.append(selected_skill2["name"])
elif level >= 5 and level <= 8:
     skillList.append(selected_skill1["name"])
     skillList.append(selected_skill2["name"])
     skillList.append(selected_skill3["name"])
     skillList.append(selected_skill4["name"])
elif level >= 9 and level <= 12:
     skillList.append(selected_skill1["name"])
     skillList.append(selected_skill2["name"])
     skillList.append(selected_skill3["name"])
     skillList.append(selected_skill4["name"])
     skillList.append(selected_skill5["name"])
     skillList.append(selected_skill6["name"])
elif level >= 13 and level <= 16:
     skillList.append(selected_skill1["name"])
     skillList.append(selected_skill2["name"])
     skillList.append(selected_skill3["name"])
     skillList.append(selected_skill4["name"])
     skillList.append(selected_skill5["name"])
     skillList.append(selected_skill6["name"])
     skillList.append(selected_skill7["name"])
     skillList.append(selected_skill8["name"])
elif level >= 17 and level <= 20:
     skillList.append(selected_skill1["name"])
     skillList.append(selected_skill2["name"])
     skillList.append(selected_skill3["name"])
     skillList.append(selected_skill4["name"])
     skillList.append(selected_skill5["name"])
     skillList.append(selected_skill6["name"])
     skillList.append(selected_skill7["name"])
     skillList.append(selected_skill8["name"])
     skillList.append(selected_skill9["name"])
     skillList.append(selected_skill10["name"])

skillNames = [name for name in skillList]
    