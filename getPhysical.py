import random
import requests
import getRace
import getClass

classes = (getClass.selected_class["name"])
race = (getRace.selected_race["name"])
male = 0
female = 0
gender_roll = random.randint(1, 2)
if gender_roll == 1:
    gender = "Male"
else:
    gender = "Female"
    
height = 0
weight = 0

# Height and Weight Ratios for D&D 5th Edition Races
if race == "Dragonborn":
    if gender == "Male":
        base_height = 60
        height_modifier = random.randint(2, 24)
        base_weight = 140
        weight_modifier = random.randint(1, 110)
    else:
        base_height = 61
        height_modifier = random.randint(2, 8)
        base_weight = 130
        weight_modifier = random.randint(2, 6)
elif race == "Dwarf":
    if gender == "Male":
        base_height = 44
        height_modifier = random.randint(2, 4)
        base_weight = 115
        weight_modifier = random.randint(2, 6)
    else:
        base_height = 42
        height_modifier = random.randint(2, 4)
        base_weight = 90
        weight_modifier = random.randint(2, 6)
elif race == "Elf" or race == "High-Elf" or race == "Wood-Elf" or race == "Dark-Elf":
    if gender == "Male":
        base_height = 56
        height_modifier = random.randint(2, 10)
        base_weight = 110
        weight_modifier = random.randint(1, 4)
    else:
        base_height = 54
        height_modifier = random.randint(2, 10)
        base_weight = 90
        weight_modifier = random.randint(1, 4)
elif race == "Gnome":
    if gender == "Male":
        base_height = 35
        height_modifier = random.randint(2, 4)
        base_weight = 35
        weight_modifier = random.randint(1, 2)
    else:
        base_height = 33
        height_modifier = random.randint(2, 4)
        base_weight = 40
        weight_modifier = random.randint(1, 2)
elif race == "Half-Elf":
    if gender == "Male":
        base_height = 57
        height_modifier = random.randint(2, 8)
        base_weight = 110
        weight_modifier = random.randint(1, 4)
    else:
        base_height = 53
        height_modifier = random.randint(2, 8)
        base_weight = 90
        weight_modifier = random.randint(1, 4)
elif race == "Half-Orc":
    if gender == "Male":
        base_height = 68
        height_modifier = random.randint(0, 25)
        base_weight = 160
        weight_modifier = random.randint(0, 140)
    else:
        base_height = 60
        height_modifier = random.randint(0, 20)
        base_weight = 120
        weight_modifier = random.randint(0, 100)
elif race == "Halfling":
    if gender == "Male":
        base_height = 31
        height_modifier = random.randint(2, 4)
        base_weight = 35
        weight_modifier = random.randint(1, 2)
    else:
        base_height = 29
        height_modifier = random.randint(2, 4)
        base_weight = 40
        weight_modifier = random.randint(1, 2)
elif race == "Human":
    if gender == "Male":
        base_height = 60
        height_modifier = random.randint(0, 20)
        base_weight = 140
        weight_modifier = random.randint(0, 100)
    else:
        base_height = 62
        height_modifier = random.randint(0, 14)
        base_weight = 90
        weight_modifier = random.randint(0, 100)
elif race == "Tiefling":
    if gender == "Male":
        base_height = 67
        height_modifier = random.randint(2, 8)
        base_weight = 140
        weight_modifier = random.randint(2, 6)
    else:
        base_height = 62
        height_modifier = random.randint(2, 8)
        base_weight = 90
        weight_modifier = random.randint(2, 6)


height = base_height + height_modifier
weight = base_weight + weight_modifier

# Take input from the user
inches = height

# Convert inches to feet and inches
feet = inches // 12
inches = inches % 12

# Print the result


eyecolors = ['Amber', 'Blue', 'Brown',
             'Gray', 'Green', 'Hazel', 'Red', 'Violet']
haircolors = ["Black", "Blonde", "Brown", "Red", "White", "Gray", "Silver", "Gold", "Green", "Blue", "Purple", "Pink", "Orange", "Yellow", "Copper", "Bronze", "Platinum", "Magenta",
              "Cyan", "Teal", "Maroon", "Mauve", "Taupe", "Beige", "Tan", "Bistre", "Burgundy", "Charcoal", "Chestnut", "Copper", "Crimson", "Fuchsia", "Golden", "Ivory", "Lavender", "Lemon", "Lilac"]
eyes = random.choice(eyecolors)
hair = random.choice(haircolors)


# print(height, ", ", weight)
# print(base_height, ", ", height_modifier, ", ", base_weight, ", ", weight_modifier)