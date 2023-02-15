import requests
import random
import getCharacterLevel

# If the class is a spellcaster, this will randomly select a spell from the D&D 5e API.  The number of spells depends on the level of the spellcaster.

level = getCharacterLevel.character_level

if level < 4:
    spellLevel = 1
elif level >= 5 and level <= 8:
    spellLevel = 2
elif level >= 9 and level <= 12:
    spellLevel = 3
elif level >= 13 and level <= 16:
    spellLevel = 4
else:
    spellLevel = 5

urlSpells = "https://www.dnd5eapi.co/api/spells"
response = requests.get(urlSpells)
data = response.json()
spells = data["results"]
selected_spells1 = random.choice(spells)
selected_spells2 = random.choice(spells)
selected_spells3 = random.choice(spells)
selected_spells4 = random.choice(spells)
selected_spells5 = random.choice(spells)


class getSpells:
    def __init__(self):
        self.spellBook = []

    def addSpell(self):
        if level >= 1 and level <= 4:
            self.spellBook.append(selected_spells1["name"])
        elif level >= 5 and level <= 8:
            self.spellBook.append(selected_spells1["name"])
            self.spellBook.append(selected_spells2["name"])
        elif level >= 9 and level <= 12:
            self.spellBook.append(selected_spells1["name"])
            self.spellBook.append(selected_spells2["name"])
            self.spellBook.append(selected_spells3["name"])
        elif level >= 13 and level <= 16:
            self.spellBook.append(selected_spells1["name"])
            self.spellBook.append(selected_spells2["name"])
            self.spellBook.append(selected_spells3["name"])
            self.spellBook.append(selected_spells4["name"])
        elif level >= 17 and level <= 20:
            self.spellBook.append(selected_spells1["name"])
            self.spellBook.append(selected_spells2["name"])
            self.spellBook.append(selected_spells3["name"])
            self.spellBook.append(selected_spells4["name"])
            self.spellBook.append(selected_spells5["name"])

    def printSpell(self):
        return [name for name in self.spellBook[:spellLevel]]


inventory = getSpells()

for i in range(getCharacterLevel.character_level):
    inventory.addSpell()

spell_string = ", ".join(inventory.printSpell())
