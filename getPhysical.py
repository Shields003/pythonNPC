import random
import requests
import getRace
import getClass

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

if race == ["Half-Orc"]:
    height = int(height * 1.3)
    weight = random.randint(220, 450)
elif race == ["Dwarf"]:
    height = height - 1
    weight = weight - 20
elif race == ["Halfling"]:
    height = height - 2
    weight = weight - 60
elif race == ["Gnome"]:
    height = height - 2
    weight = weight - 60
elif race == ["Half-Elf"] or race == ["High-Elf"] or race == ["Wood-Elf"]:
    height = height - .5
    weight = weight - 35
elif gender == 2:
    weight = int(weight*.61)
    height = int(height*.82)
    gender = "Female"
else:
    gender = "Male"


eyecolors = ['Amber', 'Blue', 'Brown',
             'Gray', 'Green', 'Hazel', 'Red', 'Violet']
haircolors = ["Black", "Blonde", "Brown", "Red", "White", "Gray", "Silver", "Gold", "Green", "Blue", "Purple", "Pink", "Orange", "Yellow", "Copper", "Bronze", "Platinum", "Magenta",
              "Cyan", "Teal", "Maroon", "Mauve", "Taupe", "Beige", "Tan", "Bistre", "Burgundy", "Charcoal", "Chestnut", "Copper", "Crimson", "Fuchsia", "Golden", "Ivory", "Lavender", "Lemon", "Lilac"]
eyes = random.choice(eyecolors)
hair = random.choice(haircolors)
