import requests
import random
import getRace
import getClass

classes = getClass.selected_class["name"]
race = getRace.selected_race["name"]

# Strength
str_dice_rolls = [random.randint(1, 6) for _ in range(4)]
dex_dice_rolls = [random.randint(1, 6) for _ in range(4)]
wis_dice_rolls = [random.randint(1, 6) for _ in range(4)]
con_dice_rolls = [random.randint(1, 6) for _ in range(4)]
int_dice_rolls = [random.randint(1, 6) for _ in range(4)]
cha_dice_rolls = [random.randint(1, 6) for _ in range(4)]

str_dice_rolls.remove(min(str_dice_rolls))
int_dice_rolls.remove(min(int_dice_rolls))
wis_dice_rolls.remove(min(wis_dice_rolls))
con_dice_rolls.remove(min(con_dice_rolls))
dex_dice_rolls.remove(min(dex_dice_rolls))
cha_dice_rolls.remove(min(cha_dice_rolls))

strength = sum(str_dice_rolls)
dexterity = sum(dex_dice_rolls)
constitution = sum(con_dice_rolls)
intelligence = sum(int_dice_rolls)
wisdom = sum(wis_dice_rolls)
charisma = sum(cha_dice_rolls)

# print ("Strength:     ", strength)
# print ("Dexterity:    ", dexterity)
# print ("Constitution: ", constitution)
# print ("Intelligence: ", intelligence)
# print ("Wisdom:       ", wisdom)
# print ("Charisma:     ", charisma)

# if race == "Dwarf": strength = strength + 1 and constitution = constitution + 2.

if race == "Dwarf":
    strength += 1
    constitution += 2
    charisma -= 1
elif race == "Elf" or race == "High-Elf" or race == "Wood-Elf":
    dexterity += 2
    intelligence += 1
elif race == "Half-Orc":
    strength += 2
    constitution += 1
    intelligence -= 1
elif race == "Gnome":
    strength -= 1
    intelligence += 2
    dexterity += 1
elif race == "Half-Elf":
    dexterity += 1
    charisma += 2
    strength -= 1
elif race == "Halfling":
    intelligence += 1
    wisdom += 2
    strength -= 1
elif race == "Tiefling":
    constitution += 1
    intelligence += 1
    charisma += 1
    wisdom -= 1
if race == "Dragonborn":
    strength += 2
    intelligence += 1
    wisdom -= 1


if classes == "Fighter" or classes == "Barbarian" or classes == "Paladin":
    if strength < 12:
        strength = 12

if classes == "Rogue" or classes == "Monk" or classes == "Ranger":
    if dexterity < 12:
        dexterity = 12

if classes == "Wizard" or classes == "Sorcerer" or classes == "Warlock":
    if intelligence < 12:
        intelligence = 12

if classes == "Cleric" or classes == "Druid":
    if wisdom < 12:
        wisdom = 12

if classes == "Bard":
    if charisma < 12:
        charisma = 12

# Stats get plus 1 strenghtBonus point for every 2 points above 10.

strengthBonus = 0
dexterityBonus = 0
constitutionBonus = 0
intelligenceBonus = 0
wisdomBonus = 0
charismaBonus = 0


def getBonus():
    if strength or dexterity or constitution or intelligence or wisdom or charisma > 10:
        strengthBonus = (strength - 10) // 2
        dexterityBonus = (dexterity - 10) // 2
        constitutionBonus = (constitution - 10) // 2
        intelligenceBonus = (intelligence - 10) // 2
        wisdomBonus = (wisdom - 10) // 2
        charismaBonus = (charisma - 10) // 2
        if strengthBonus > 0 or strengthBonus < 0:
            print("Strength:     ", strength, "(+ ", strengthBonus, ")")
        if dexterityBonus > 0 or dexterityBonus < 0:
            print("Dexterity:    ", dexterity, "(+ ", dexterityBonus, ")")
        if constitutionBonus > 0 or constitutionBonus < 0:
            print("Constitution: ", constitution,
                  "(+ ", constitutionBonus, ")")
        if intelligenceBonus > 0 or intelligenceBonus < 0:
            print("Intelligence: ", intelligence,
                  "(+ ", intelligenceBonus, ")")
        if wisdomBonus > 0 or wisdomBonus < 0:
            print("Wisdom:       ", wisdom, "(+ ", wisdomBonus, ")")
        if charismaBonus > 0 or charismaBonus < 0:
            print("Charisma:     ", charisma, "(+ ", charismaBonus, ")")
 
    else:
        print("Strength:     ", strength)
        print("Dexterity:    ", dexterity)
        print("Constitution: ", constitution)
        print("Intelligence: ", intelligence)
        print("Wisdom:       ", wisdom)
        print("Charisma:     ", charisma)
