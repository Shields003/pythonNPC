# Imports
import requests
import random
from getStats import generate_stats
import birthData
import getPhobia
import getInsanity
import getSpells
import getAlignment
import getBackground
import getSkills
import getEquipment
import getClass
from getRace import generate_race
import getCharacterLevel
import getWeapon
import getArmor
import getPhysical
import getFear
import getProficiencies
import getPokemon
import getSkillProf
from getName import generate_name
from getBackground import generate_backstory


def generate_character():
    race = generate_race()
    gender = getPhysical.gender
    classes = getClass.selected_class["name"]  # Define classes here
    name = generate_name(race, gender)  # Generate the name here
    my_backstory = generate_backstory()
    attributes, bonus_points, speed = generate_stats(race, classes)

    # Variables
    weight = getPhysical.weight
    height = getPhysical.height
    feet = getPhysical.feet
    inches = getPhysical.inches
    level = getCharacterLevel.character_level
    eyes = getPhysical.eyes
    hair = getPhysical.hair
    age = birthData.age
    bmonth = birthData.bmonth
    bday = birthData.bday
    birth_year = birthData.birthyear
    zodiac = birthData.zodiac
    fear = (getFear.get_type + " " + getFear.focus)
    proficiencies = getProficiencies.proficiency_string
    savethrow = 11

    # Stats
    strength = attributes['strength']
    strength_bonus = bonus_points.get('strength', 0)
    dexterity = attributes['dexterity']
    dexterity_bonus = bonus_points.get('dexterity', 0)
    constitution = attributes['constitution']
    constitution_bonus = bonus_points.get('constitution', 0)
    intelligence = attributes['intelligence']
    intelligence_bonus = bonus_points.get('intelligence', 0)
    wisdom = attributes['wisdom']
    wisdom_bonus = bonus_points.get('wisdom', 0)
    charisma = attributes['charisma']
    charisma_bonus = bonus_points.get('charisma', 0)

    # Items
    weapon = getWeapon.Weapon()
    weapon.get_weapon_data()

    # AC = 10 + DEX + Armor
    armor_name, armor_class = getArmor.get_armor()
    ac = 10 + dexterity_bonus + armor_class  # Calculate AC here

    # Here is where we return the NPC as a dictionary
    return {
        "name": name,  # Use the name variable here
        "race": race,
        "class": classes,
        "gender": gender,
        "weight": weight,
        "height": height,
        "feet": feet,
        "inches": inches,
        "level": level,
        "eyes": eyes,
        "hair": hair,
        "speed": speed,
        "age": age,
        "bmonth": bmonth,
        "bday": bday,
        "birth_year": birth_year,
        "zodiac": zodiac,
        "fear": fear,
        "proficiencies": proficiencies,
        "strength": strength,
        "strength_bonus": strength_bonus,
        "dexterity": dexterity,
        "dexterity_bonus": dexterity_bonus,
        "constitution": constitution,
        "constitution_bonus": constitution_bonus,
        "intelligence": intelligence,
        "intelligence_bonus": intelligence_bonus,
        "wisdom": wisdom,
        "wisdom_bonus": wisdom_bonus,
        "charisma": charisma,
        "charisma_bonus": charisma_bonus,
        "weapon": weapon.selected_weapon["name"],
        "weapon_damage": weapon.damage_dice,
        "offhand_weapon": weapon.selected_weapon2["name"],
        "offhand_weapon_damage": weapon.damage_dice2,
        "armor_name": armor_name,
        "armor_class": armor_class,
        "ac": ac,
        "backstory": my_backstory
    }
