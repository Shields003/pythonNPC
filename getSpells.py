import requests
import random
import getCharacterLevel

# If the class is a spellcaster, this will randomly select a spell from the D&D 5e API.  The number of spells depends on the level of the spellcaster.

spell_level = getCharacterLevel.character_level

if spell_level < 4:
    spellLevel = 1
elif spell_level >= 5 and spell_level <= 8:
    spellLevel = 2
elif spell_level >= 9 and spell_level <= 12:
    spellLevel = 3
elif spell_level >= 13 and spell_level <= 16:
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


class get_spells:
    def __init__(self):
        self.spell_book = []

    def add_spell(self):
        if spell_level >= 1 and spell_level <= 4:
            self.spell_book.append(selected_spells1["name"])
        elif spell_level >= 5 and spell_level <= 8:
            self.spell_book.append(selected_spells1["name"])
            self.spell_book.append(selected_spells2["name"])
        elif spell_level >= 9 and spell_level <= 12:
            self.spell_book.append(selected_spells1["name"])
            self.spell_book.append(selected_spells2["name"])
            self.spell_book.append(selected_spells3["name"])
        elif spell_level >= 13 and spell_level <= 16:
            self.spell_book.append(selected_spells1["name"])
            self.spell_book.append(selected_spells2["name"])
            self.spell_book.append(selected_spells3["name"])
            self.spell_book.append(selected_spells4["name"])
        elif spell_level >= 17 and spell_level <= 20:
            self.spell_book.append(selected_spells1["name"])
            self.spell_book.append(selected_spells2["name"])
            self.spell_book.append(selected_spells3["name"])
            self.spell_book.append(selected_spells4["name"])
            self.spell_book.append(selected_spells5["name"])

    def print_spell(self):
        return [name for name in self.spell_book[:spell_level]]


inventory = get_spells()

for i in range(getCharacterLevel.character_level):
    inventory.add_spell()

spell_string = ", ".join(inventory.print_spell())
