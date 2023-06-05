import requests
import random

try:
    import getRace
    import getClass
except ImportError as e:
    print(f"Error importing module: {e}")
    exit(1)

try:
    classes = getClass.selected_class["name"]
    race = getRace.selected_race["name"]
except KeyError as e:
    print(f"Error accessing class or race attribute: {e}")
    exit(1)

# Speed
speed = 30

# Strength
str_dice_rolls = [random.randint(1, 6) for _ in range(4)]
dex_dice_rolls = [random.randint(1, 6) for _ in range(4)]
wis_dice_rolls = [random.randint(1, 6) for _ in range(4)]
con_dice_rolls = [random.randint(1, 6) for _ in range(4)]
int_dice_rolls = [random.randint(1, 6) for _ in range(4)]
cha_dice_rolls = [random.randint(1, 6) for _ in range(4)]

dice_rolls = {
    "strength": str_dice_rolls,
    "dexterity": dex_dice_rolls,
    "wisdom": wis_dice_rolls,
    "constitution": con_dice_rolls,
    "intelligence": int_dice_rolls,
    "charisma": cha_dice_rolls,
}

# Remove the minimum roll for each attribute
for attribute, rolls in dice_rolls.items():
    dice_rolls[attribute].remove(min(rolls))

# Sum the dice rolls for each attribute
attributes = {attribute: sum(rolls) for attribute, rolls in dice_rolls.items()}

# Define race modifiers
race_modifiers = {
    "Dwarf": {"strength": 1, "constitution": 2, "charisma": -1},
    "Elf": {"dexterity": 2, "intelligence": 1},
    "High-Elf": {"dexterity": 2, "intelligence": 1},
    "Wood-Elf": {"dexterity": 2, "intelligence": 1},
    "Half-Orc": {"strength": 2, "constitution": 1, "intelligence": -1},
    "Gnome": {"strength": -1, "intelligence": 2, "dexterity": 1},
    "Half-Elf": {"dexterity": 1, "charisma": 2, "strength": -1},
    "Halfling": {"intelligence": 1, "wisdom": 2, "strength": -1},
    "Tiefling": {"constitution": 1, "intelligence": 1, "charisma": 1, "wisdom": -1},
    "Dragonborn": {"strength": 2, "intelligence": 1, "wisdom": -1},
}

# Apply race modifiers
for attribute, modifier in race_modifiers.get(race, {}).items():
    attributes[attribute] += modifier

# Define minimum class attributes
class_minimums = {
    "Fighter": {"strength": 12},
    "Barbarian": {"strength": 12},
    "Paladin": {"strength": 12},
    "Rogue": {"dexterity": 12},
    "Monk": {"dexterity": 12},
    "Ranger": {"dexterity": 12},
    "Wizard": {"intelligence": 12},
    "Sorcerer": {"intelligence": 12},
    "Warlock": {"intelligence": 12},
    "Cleric": {"wisdom": 12},
    "Druid": {"wisdom": 12},
    "Bard": {"charisma": 12},
}

# Ensure class minimums
for attribute, minimum in class_minimums.get(classes, {}).items():
    attributes[attribute] = max(attributes[attribute], minimum)

# Clamp attributes to the range 1-20
for attribute, value in attributes.items():
    attributes[attribute] = min(max(value, 1), 20)

# Stats get plus 1 bonus point for every 2 points above 10
bonus_points = {attribute: (value - 10) // 2 for attribute, value in attributes.items() if value > 10}

strengthBonus = bonus_points.get('strength', 0)
dexterityBonus = bonus_points.get('dexterity', 0)
constitutionBonus = bonus_points.get('constitution', 0)
intelligenceBonus = bonus_points.get('intelligence', 0)
wisdomBonus = bonus_points.get('wisdom', 0)
charismaBonus = bonus_points.get('charisma', 0)
