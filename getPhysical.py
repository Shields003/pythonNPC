import random


def generate_gender():
    genders = ["Male", "Female"]
    return random.choice(genders)


gender = generate_gender()


def generate_height_weight(race, gender):
    height = 0
    weight = 0
    base_height = 0
    height_modifier = 0
    base_weight = 0
    weight_modifier = 0

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
            base_height = 50
            height_modifier = random.randint(2, 8)
            base_weight = 115
            weight_modifier = random.randint(2, 6)
        else:
            base_height = 42
            height_modifier = random.randint(2, 4)
            base_weight = 90
            weight_modifier = random.randint(2, 6)
    elif race == "Elf" or race == "High-Elf" or race == "Wood-Elf" or race == "Dark-Elf":
        if gender == "Male":
            base_height = 59
            height_modifier = random.randint(2, 10)
            base_weight = 110
            weight_modifier = random.randint(1, 4)
        else:
            base_height = 55
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

    height = base_height + height_modifier
    weight = base_weight + weight_modifier

    return height, weight


def generate_eye_color():
    eye_colors = ["Amber", "Blue", "Brown", "Gray",
                  "Green", "Hazel", "Red", "Violet", "Black"]
    return random.choice(eye_colors)


def generate_hair_color():
    hair_colors = [
        "Black", "Blonde", "Brown", "Red", "White", "Gray", "Silver", "Gold", "Green",
        "Blue", "Purple", "Pink", "Orange", "Yellow", "Copper", "Bronze", "Platinum",
        "Magenta", "Cyan", "Teal", "Maroon", "Mauve", "Taupe", "Beige", "Tan", "Bistre",
        "Burgundy", "Charcoal", "Chestnut", "Copper", "Crimson", "Fuchsia", "Golden",
        "Ivory", "Lavender", "Lemon", "Lilac"
    ]
    return random.choice(hair_colors)
