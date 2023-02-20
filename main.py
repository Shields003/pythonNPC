# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:50:01 2020

@author: Owner
"""

# Imports
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
import getCharacterLevel
import getWeapon
import getArmor
import getPhysical
import getFear
import getProficiencies
import getPokemon

# Variables
classes = (getClass.selected_class["name"])
race = (getRace.selected_race["name"])
gender = getPhysical.gender
weight = getPhysical.weight
height = getPhysical.height
feet = getPhysical.feet
inches = getPhysical.inches
level = getCharacterLevel.character_level
eyes = getPhysical.eyes
hair = getPhysical.hair
speed = getStats.speed
age = birthData.age
bmonth = birthData.bmonth
bday = birthData.bday
birth_year = birthData.birthyear
zodiac = birthData.zodiac
fear = (getFear.get_type + " " + getFear.focus)
ac = 10
proficiencies = getProficiencies.proficiency_string
race = getRace.selected_race["name"]
# armor_class = getArmor.ac
# ac = armor_class + getStats.dexterityBonus

savethrow = 11
savethrow = savethrow

# Here is where we print out the NPC
print("-------------------------------")
print("-------------------------------")
print("Dungeons & Dragons Random NPC Generator!")
print("-------------------------------")
print("Race:        ", getRace.selected_race["name"])
print("Class:       ", getClass.selected_class["name"])
print("Alignment:   ", getAlignment.selectedAlignment["name"])
print("Level:       ", level)
print("-------------------------------")
getStats.getBonus()
print("-------------------------------")
print('Gender:      ', getPhysical.gender)
print("Age:         ", age)
print("Birth Day:   ", bmonth, "", bday, ", ", birth_year)
print("Zodiac:      ", zodiac)
print("Weight:      ", weight, "lbs")
print(f"Height:       {feet} feet {inches} inches")
print('Eye Color:   ', eyes, '  Hair Color:', hair)
print("Speed        ", speed)
print("-------------------------------")
print("Phobia:      ", getPhobia.phobia)
print("Insanity:    ", getInsanity.insanity)
print("Background:   " + getBackground.background)
print("Other:       ", fear)
print("Favorite Pokemon: ", getPokemon.capitalized_pokemon)
print("-------------------------------")
print("AC:          ", getArmor.ac)
print("Armor:       ", getArmor.armor_name)
print("-------------------------------")
print("Saving Throw:", getProficiencies.saving_throw_list)
print("-------------------------------")
print("Weapon:          ", getWeapon.selected_weapon["name"])
print("Off-Hand Weapon: ", getWeapon.selected_weapon2["name"])
print("-------------------------------")
print("Spells:", getSpells.spell_string)
print("-------------------------------")
print("Proficiencies: ", getProficiencies.proficiency_list)
print("-------------------------------")
print("Skills: ", getSkills.skill_string)
print("-------------------------------")
print("Equipment: ", getEquipment.equipment_string)
print("-------------------------------")
print(getBackground.paragraph_one)
print("")
print(getBackground.paragraph_two)
print("-------------------------------")
