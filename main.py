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
import getSkillProf
import getName

from getBackground import generate_backstory

# Call the function and store the generated backstory in a variable
my_backstory = generate_backstory()

# Variables
name = getName.name
classes = (getClass.selected_class["name"])
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
proficiencies = getProficiencies.proficiency_string
race = getRace.selected_race["name"]
# armor_class = getArmor.ac
# ac = armor_class + getStats.dexterityBonus

savethrow = 11
savethrow = savethrow

# Stats
strength = getStats.attributes['strength']
strength_bonus = getStats.bonus_points.get('strength', 0)
dexterity = getStats.attributes['dexterity']
dexterity_bonus = getStats.bonus_points.get('dexterity', 0)
constitution = getStats.attributes['constitution']
constitution_bonus = getStats.bonus_points.get('constitution', 0)
intelligence = getStats.attributes['intelligence']
intelligence_bonus = getStats.bonus_points.get('intelligence', 0)
wisdom = getStats.attributes['wisdom']
wisdom_bonus = getStats.bonus_points.get('wisdom', 0)
charisma = getStats.attributes['charisma']
charisma_bonus = getStats.bonus_points.get('charisma', 0)


# Items
weapon = getWeapon.Weapon()

weapon.get_weapon_data()

# AC = 10 + DEX + Armor
armor_name, armor_class = getArmor.get_armor()

ac = 0
ac = ac + dexterity_bonus

# Here is where we print out the NPC
print("-------------------------------")
print("-------------------------------")
print("Dungeons & Dragons Random NPC Generator!")
print("-------------------------------")
print("Name:        ", name)
print("Race:        ", race)
print("Class:       ", getClass.selected_class["name"])
print("Alignment:   ", getAlignment.selectedAlignment["name"])
print("Level:       ", level)
print("-------------------------------")
#Stats
if strength_bonus > 0:
    print("Strength:     ", strength, "(+", strength_bonus, ")")
if strength_bonus < 0:
        print("Strength:     ", strength, " (", strength_bonus, ")")
if strength_bonus == 0:
        print("Strength:     ", strength)
if dexterity_bonus > 0:
        print("Dexterity:    ", dexterity, "(+", dexterity_bonus, ")")
if dexterity_bonus < 0:
        print("Dexterity:    ", dexterity, " (", dexterity_bonus, ")")
if dexterity_bonus == 0:
        print("Dexterity:    ", dexterity)
if constitution_bonus > 0:
        print("Constitution: ", constitution,
              "(+", constitution_bonus, ")")
if constitution_bonus < 0:
        print("Constitution: ", constitution,
              " (", constitution_bonus, ")")
if constitution_bonus == 0:
        print("Constitution: ", constitution)
if intelligence_bonus > 0:
        print("Intelligence: ", intelligence,
              "(+", intelligence_bonus, ")")
if intelligence_bonus < 0:
        print("Intelligence: ", intelligence,
              " (", intelligence_bonus, ")")
if intelligence_bonus == 0:
        print("Intelligence: ", intelligence)
if wisdom_bonus > 0:
        print("Wisdom:       ", wisdom, "(+", wisdom_bonus, ")")
if wisdom_bonus < 0:
        print("Wisdom:       ", wisdom, " (", wisdom_bonus, ")")
if wisdom_bonus == 0:
        print("Wisdom:       ", wisdom)
if charisma_bonus > 0:
        print("Charisma:     ", charisma, "(+", charisma_bonus, ")")
if charisma_bonus < 0:
        print("Charisma:     ", charisma, " (", charisma_bonus, ")")
if charisma_bonus == 0:
        print("Charisma:     ", charisma)
        

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
print("AC:          ", ac) # getArmor.armor_ac
print("Armor:       ", getArmor.armor_name)
print("-------------------------------")
# print("Saving Throw:", getProficiencies.saving_throw_list)
print("-------------------------------")
print("Weapon: ", weapon.selected_weapon["name"], "(", weapon.damage_dice,  "+", strength_bonus,")")
print("Off-Hand Weapon: ", weapon.selected_weapon2["name"], "(", weapon.damage_dice2,  "+", strength_bonus,")")
print("-------------------------------")
print("Spells:", getSpells.spell_string)
print("-------------------------------")
getSkillProf.DNDCharacter().print_proficiencies()
print("-------------------------------")
print("-------------------------------")
print("Equipment: ", getEquipment.equipment_string)
print("-------------------------------")
print(my_backstory)
print("")
print("-------------------------------")
