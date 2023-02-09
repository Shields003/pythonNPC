# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:50:01 2020

@author: Owner
"""
import requests
import random
import birthData
import getPhobia
import getInsanity
import getSpells
import getAlignment
import getBackground
import getSkills


urlClasses = "https://www.dnd5eapi.co/api/classes"

response = requests.get(urlClasses)

if response.status_code == 200:
    data = response.json()
    classes = data["results"]
    selected_class = random.choice(classes)
#     print(selected_class["name"])
else:
    print("Failed to retrieve data")

urlRaces = "https://www.dnd5eapi.co/api/races"

response = requests.get(urlRaces)

if response.status_code == 200:
    data = response.json()
    race = data["results"]
    selected_race = random.choice(race)
else:
    print("Failed to retrieve data")
    
urlWeapons = "https://www.dnd5eapi.co/api/equipment-categories/weapon"

response = requests.get(urlWeapons)

if response.status_code == 200:
    data = response.json()
    weapons = data["equipment"]
    selected_weapon = random.choice(weapons)

    selected_weapon2 = random.choice(weapons)
else:
    print("Failed to retrieve data")

# If the selected weapons name contains "Weapon" then it will select another weapon.
if "Weapon" in selected_weapon["name"]:
    selected_weapon = random.choice(weapons)

if "Weapon" in selected_weapon2["name"]:
    selected_weapon2 = random.choice(weapons)
    
    
#This gets the damage dice for the weapon.
# urlDamage = "https://www.dnd5eapi.co/api/equipment/"
# response = requests.get(urlDamage)

# if response.status_code == 200:
#     data = response.json()
#     damage_dice = data["equipment"]
    
# else:
#     print("Request failed with status code:", response.status_code)    
    
    
    
    
    
    
    
    
    


print("-------------------------------")
print("Dungeons & Dragons Random NPC Generator!")
print("-------------------------------")
# print('Name:        ', name)

# Race, Gender, Height, weight and bonuses
classes = (selected_class["name"])
race = (selected_race["name"])
age = (random.randint(1, 10))
male = 0
female = 0
gender = random.randint(1, 2)
heightinch = random.randint(1, 3)+random.randint(1, 3) + \
    random.randint(1, 3)+random.randint(1, 3)-4
height = 6
weight = (random.randint(140, 250))
weightadj = int(heightinch*1.2)
weight = weight + weightadj

# Much better to use metric or numInches
if height == 4:
    weight = random.randint(125, 175)
elif height == 5:
    weight = random.randint(150, 200)
elif height == 6:
    weight = random.randint(185, 280)
elif height == 7:
    weight = random.randint(250, 400)
elif height >= 8:
    weight = random.randint(370, 500)

if height == 4:
    fweight = random.randint(85, 150)
elif height == 5:
    fweight = random.randint(100, 200)
elif height == 6:
    fweight = random.randint(140, 240) + random.randint(11, 25)
elif height == 7:
    fweight = random.randint(215, 350)
elif height >= 8:
    fweight = random.randint(320, 420)

if race == ["halfogre"]:
    height = int(height * 1.3)

if race == ["halfogre"]:
    weight = random.randint(220, 450)

if race == ["dwarf"]:
    height = height - 1

# Generate 3d6 stats and add any race/class bonuses
# Strength
strength = (random.randint(1, 6))+(random.randint(1, 6))+(random.randint(1, 6))
if race == ['dwarf']:
    strength = strength + 1
elif race == ['highelf']:
    strength = strength - 1
elif race == ['halfogre']:
    strength = strength + 3

if classes == ["Fighter"]:
    strength = strength + (random.randint(1, 3))
elif classes == ["Paladin"]:
    strength = strength + (random.randint(1, 2))


# Intelligence
intelligence = (random.randint(1, 6)) + \
    (random.randint(1, 6))+(random.randint(1, 6))
if race == ['halfogre']:
    intelligence = intelligence - 2
elif race == ['human']:
    intelligence = intelligence + 1
elif race == ['highelf']:
    intelligence = intelligence + 2

if classes == ["Magician"]:
    intelligence = intelligence + 3


# Wisdom
wisdom = (random.randint(1, 6))+(random.randint(1, 6))+(random.randint(1, 6))
if classes == ["Cleric"]:
    wisdom = wisdom + 3


# Dexterity
dexterity = (random.randint(1, 6)) + \
    (random.randint(1, 6))+(random.randint(1, 6))
if race == ['woodelf']:
    dexterity = dexterity + 3
elif race == ['drowelf']:
    dexterity = dexterity + 2
elif race == ["highelf"]:
    dexterity = dexterity + 2
elif race == ['halfogre']:
    dexterity = dexterity - 2

if classes == ["Thief"]:
    dexterity = dexterity + 3
elif classes == ["ranger"]:
    dexterity = dexterity + 3

# Constitution
constitution = (random.randint(1, 6)) + \
    (random.randint(1, 6))+(random.randint(1, 6))
if race == ['dwarf']:
    constitution = constitution + 1
elif race == ['halfogre']:
    constitution = constitution + 2

if classes == ["Fighter"]:
    constitution = constitution + (random.randint(1, 2))
elif classes == ["Paladin"]:
    constitution = constitution + (random.randint(1, 3))
elif classes == ["Cleric"]:
    constitution = constitution + (random.randint(0, 2))

# Charisma
charisma = (random.randint(1, 6))+(random.randint(1, 6))+(random.randint(1, 6))
if race == ['dwarf']:
    charisma = charisma - 1
elif race == ['halfogre']:
    charisma = charisma - 2
elif race == ['drowelf']:
    charisma = charisma - 1

# Mutations???
statlist = ["strength", "intelligence", "wisdom",
            "dexterity", "constitution", "charisma"]
bonusstat = (random.choices(statlist))
mutation = (random.randint(-2, 8))

# Age
if race == ["drowelf"]:
    age = (random.randint(50, 130))
elif race == ["woodelf"]:
    age = (random.randint(75, 180))
elif race == ["highelf"]:
    age = (random.randint(100, 250))
elif race == ["dwarf"]:
    age = (random.randint(35, 60))
elif race == ["halfelf"]:
    age = (random.randint(24, 50))
elif race == ["halfogre"]:
    age = (random.randint(12, 19))
elif race == ["mutant"]:
    age = (random.randint(16, 25))
elif race == ["human"]:
    age = (random.randint(17, 28))

# level and age
level = random.randint(1, 20)

# Start in print out stats
# Race

print("Race:        ", selected_race["name"])

# Classes
print("Class:       ", selected_class["name"])

# Discription Level and age, print
eyecolors = ['Brown  ', 'Hazel  ', 'Blue   ', 'Grey   ',
             'Green  ', 'Red    ', 'Black  ', 'Rainbow']
haircolors = ['Brown', 'Blonde', 'Light-Brown',
              'Grey', 'Green', 'Red', 'Black', 'Rainbow']
eyes = random.choice(eyecolors)
hair = random.choice(haircolors)
speed = 30

if gender == 2:
    weight = int(weight*.61)

if gender == 2:
    height = int(height*.9)

print("Alignment:   ", getAlignment.selectedAlignment["name"])
print("Level:       ", level)
if gender == 1:
    print('Gender:       Male')
else:
    print('Gender:       Female')
print('Height:      ', height, 'ft', heightinch, 'inches', '  Weight:', weight)
print('Eye Color:   ', eyes, '        Hair Color:', hair)
print("Speed        ", speed)


# Sanity check.  The following is an array of insanity and phobias.  The program will randomly select one of each and print them out.
print("-------------------------------")
# This prints out a random phobia from getPhobia.py

print("-------------------------------")

# The following code adds a bonus for every 2 points in a stat above 10
strbonus = 0
dexbonus = 0
conbonus = 0
intbonus = 0
wisbonus = 0
chabonus = 0


if strength >= 12:
    strbonus = (strength - 10) / 2
    strbonus = int(strbonus)

if dexterity >= 12:
    dexbonus = (dexterity - 10) / 2
    dexbonus = int(dexbonus)

if constitution >= 12:
    conbonus = (constitution - 10) / 2
    conbonus = int(conbonus)

if intelligence >= 12:
    intbonus = (intelligence - 10) / 2
    intbonus = int(intbonus)

if wisdom >= 12:
    wisbonus = (wisdom - 10) / 2
    wisbonus = int(wisbonus)

if charisma >= 12:
    chabonus = (charisma - 10) / 2
    chabonus = int(chabonus)

# The following code subtracts 1 for every 2 points below 11.

if strength < 12:
    strbonus = (strength - 11) / 2
    strbonus = int(strbonus)

if dexterity < 12:
    dexbonus = (dexterity - 11) / 2
    dexbonus = int(dexbonus)

if constitution < 12:
    conbonus = (constitution - 11) / 2
    conbonus = int(conbonus)

if intelligence < 12:
    intbonus = (intelligence - 11) / 2
    intbonus = int(intbonus)

if wisdom < 12:
    wisbonus = (wisdom - 11) / 2
    wisbonus = int(wisbonus)

if charisma < 12:
    chabonus = (charisma - 11) / 2
    chabonus = int(chabonus)

# Bob

# The following code prints the stats and bonuses
# High Stat bonuses
if strength >= 16:
    print("Strength:    ", strength, "(+", strbonus, "Bonus)")
else:
    print("Strength:    ", strength)

if intelligence >= 16:
    print("Intelligence:", intelligence, "(+", intbonus, "Bonus)")
else:
    print("Intelligence:", intelligence)

if wisdom >= 16:
    print("Wisdom:      ", wisdom, "(+", wisbonus, "Bonus)")
else:
    print("Wisdom:      ", wisdom)

if dexterity >= 16:
    print("Dexterity:   ", dexterity, "(+", dexbonus, "Bonus)")
else:
    print("Dexterity:   ", dexterity)

if constitution >= 16:
    print("Constitution:", constitution, "(+", conbonus, "Bonus)")
else:
    print("Constitution:", constitution)

if charisma >= 16:
    print("Charisma:    ", charisma, "(+", chabonus, "Bonus)")
else:
    print("Charisma:    ", charisma)

print("-------------------------------")

# Race bonuses print line
if race == ["highelf"]:
    print("High-Elf Racial bonuses: Int +2, Dex +2, Str -1")
elif race == ["woodelf"]:
    print("Wood-Elf Racial bonuses: Dex +3")
elif race == ["dwarf"]:
    print("Dwarf Racial Bonus: Str +2, Con +1, Cha -1, speed - 2d8")
elif race == ["halfelf"]:
    print("Half-elf Racial Bonus: Dex +1")
elif race == ["halfogre"]:
    print("Half-ogre Racial Bonus: Str +3, Con +2, Dex - 1, Cha -2")
elif race == ["drowelf"]:
    print("Drow Racial Bonus: Str +1, Dex +2, Cha -1")
elif race == ["human"]:
    print("Human Racial Bonus: Int +1, Plus 5% Exp, 1 Additional Class skill")
elif race == ["mutant"]:
    print("Mutant Racial Bonus:", bonusstat, "+", mutation)
print("-------------------------------")


# Weapons

# weapon =(selected_weapon["name"])
# print("Weapons:      ", weapon)

# spells
spellone = ["magic missiles", "find object", "minor illusion"]
spelltwo = ["fireball", "minor levetation", "shocking grasp"]

numspells = level + 1
knownspellsone = (random.choices(spellone))
knownspellstwo = (random.choices(spelltwo))

if classes == ["Magician"]:
    print("Spells:", knownspellsone)
    print(knownspellstwo)


print("Phobia:      ", getPhobia.phobia)
print("Insanity:    ", getInsanity.insanity)

print("-------------------------------")


# Zodiac and birthdates
# this prints data from the birthData.py module.
print("Age:         ", birthData.age)
print("Zodiac:      ", birthData.zodiacSign)
print("Birth Year:  ", birthData.birthyear)
print("Background:  ", getBackground.selectedBackground["name"])
print("-------------------------------")
# AC, Saving Throws, and THACO
armor = 4

ac = dexbonus+armor
print("AC:      ", ac)

thaco = 11
thaco = thaco - (dexbonus + strbonus)
print("THACO:   ", thaco)

print("-----------------------")
print("Saving Throws")

savethrow = 11
savethrow = savethrow - conbonus

print(savethrow)

print("-------------------------------")
print("Weapon:          ", selected_weapon["name"])

print("Off-Hand Weapon: ", selected_weapon2["name"])

print("-------------------------------")
print("-------------------------------")
print("Spells:", getSpells.spellBook)
print("-------------------------------")
print("Skills: ", getSkills.skillList)
print(getSkills.skillNames)