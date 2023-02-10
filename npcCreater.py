# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:50:01 2020

@author: Owner
"""
import requests
import random
import getStats
import birthData
import getPhobia
import getInsanity
import getSpells
import getAlignment
import getBackground
import getSkills
import getEquipment
import getClass
import getRace


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


print("-------------------------------")
print("Dungeons & Dragons Random NPC Generator!")
print("-------------------------------")

# Race, Gender, Height, weight and bonuses
classes = (getClass.selected_class["name"])
race = (getRace.selected_race["name"])
male = 0
female = 0
gender = random.randint(1, 2)
heightinch = random.randint(1, 3)+random.randint(1, 3) + \
    random.randint(1, 3)+random.randint(1, 3)-4
height = 6
weight = (random.randint(140, 250))
weightadj = int(heightinch*1.2)
weight = weight + weightadj

# Generate a random height and weight
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


# If the class is a fighter, barbarian or paladin, then the minimum strength is 12.


# level and age
level = random.randint(1, 20)

# Start in print out stats
# Race

# print("Race:        ", selected_race["name"])
print("Race:        ", getRace.selected_race["name"])

# Classes
print("Class:       ", getClass.selected_class["name"])

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

print(getStats.getBonus())



#Here are the ability scores.  They are randomly generated in getStats.py


print("-------------------------------")

#Phobia and insanity tables
print("Phobia:      ", getPhobia.phobia)
print("Insanity:    ", getInsanity.insanity)
print("-------------------------------")

# Zodiac and birthdates
# this prints data from the birthData.py module.
age = birthData.age
print(birthData.printBirthData())
print("Background:  ", getBackground.selectedBackground["name"])
print("-------------------------------")

# AC, Saving Throws, and THACO
armor = 11 + getStats.dexterityBonus
ac = armor
print("AC:      ", ac)

#Saving Throws
print("-----------------------")
print("Saving Throws")
savethrow = 11
savethrow = savethrow
print(savethrow)
print("-------------------------------")

#Weapon and Off-Hand Weapon
print("Weapon:          ", selected_weapon["name"])
print("Off-Hand Weapon: ", selected_weapon2["name"])
print("-------------------------------")
print("Spells:", getSpells.printSpells())
print("-------------------------------")
print("Skills: ", getSkills.skill_string)
print("-------------------------------")

# prints out the equipment from the getEquipment.py module
print("Equipment: ", getEquipment.equipment_string)
print("-------------------------------")
print("-------------------------------")
