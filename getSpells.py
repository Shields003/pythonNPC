import requests
import random


# If the class is a spellcaster, this will randomly select a spell from the D&D 5e API.  The number of spells depends on the level of the spellcaster.


urlSpells = "https://www.dnd5eapi.co/api/spells"
response = requests.get(urlSpells)
data = response.json()
spells = data["results"]
selected_spells1 = random.choice(spells)
selected_spells2 = random.choice(spells)
selected_spells3 = random.choice(spells)
selected_spells4 = random.choice(spells)
selected_spells5 = random.choice(spells)
level = random.randint(1, 20)

spellBook = []

if level >= 1 and level <= 4:
    spellBook.append(selected_spells1["name"])
elif level >= 5 and level <= 8:
    spellBook.append(selected_spells1["name"])
    spellBook.append(selected_spells2["name"])
elif level >= 9 and level <= 12:
    spellBook.append(selected_spells1["name"])
    spellBook.append(selected_spells2["name"])
    spellBook.append(selected_spells3["name"])
elif level >= 13 and level <= 16:
    spellBook.append(selected_spells1["name"])
    spellBook.append(selected_spells2["name"])
    spellBook.append(selected_spells3["name"])
    spellBook.append(selected_spells4["name"])
elif level >= 17 and level <= 20:
    spellBook.append(selected_spells1["name"])
    spellBook.append(selected_spells2["name"])
    spellBook.append(selected_spells3["name"])
    spellBook.append(selected_spells4["name"])
    spellBook.append(selected_spells5["name"])
    

spellNames = [name for name in spellBook]

def printSpells():
    for spell in spellNames:
        print(spell)
        
    
# this function will dynamically add the spell to the character's spell list based on the class and level of the character.
