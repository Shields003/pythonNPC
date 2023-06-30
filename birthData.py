# Zodiac and birthdates
import random
import requests

from getRace import generate_race

age = 0


def getAge(race):
    # Age
    if race == "Dwarf":
        age = random.randint(50, 350)
    elif race == "Elf" or race == "High-Elf" or race == "Wood-Elf" or race == "Dark-Elf":
        age = random.randint(100, 750)
    elif race == "Half-Orc":
        age = random.randint(14, 75)
    elif race == "Halfling":
        age = random.randint(20, 120)
    elif race == "Human":
        age = random.randint(18, 50)
    elif race == "Dragonborn":
        age = random.randint(15, 80)
    elif race == "Gnome":
        age = random.randint(40, 500)
    elif race == "Half-Elf":
        age = random.randint(20, 120)
    elif race == "Tiefling":
        age = random.randint(18, 60)
    elif race == "Goliath":
        age = random.randint(16, 80)
    else:
        age = random.randint(18, 50)

    return age


race = generate_race()
age = getAge(race)

birthyear = 0
bday = 0
birthyear = 623 - age

# Generate a random birth year between 1900 and 2023
birth_year = 500 - age
julian_bday = random.randint(1, 365)

if julian_bday <= 31:
    bmonth = "January"
    bday = julian_bday
    if bday >= 19:
        zodiac = "Capricorn"
    else:
        zodiac = "Aquarius"
elif julian_bday <= 59:
    bmonth = "February"
    bday = julian_bday - 31
    if bday >= 18:
        zodiac = "Aquarius"
    else:
        zodiac = "Pisces"
elif julian_bday <= 90:
    bmonth = "March"
    bday = julian_bday - 59
    if bday >= 20:
        zodiac = "Pisces"
    else:
        zodiac = "Aries"
elif julian_bday <= 120:
    bmonth = "April"
    bday = julian_bday - 90
    if bday >= 19:
        zodiac = "Aries"
    else:
        zodiac = "Taurus"
elif julian_bday <= 151:
    bmonth = "May"
    bday = julian_bday - 120
    if bday >= 20:
        zodiac = "Taurus"
    else:
        zodiac = "Gemini"
elif julian_bday <= 181:
    bmonth = "June"
    bday = julian_bday - 151
    if bday >= 20:
        zodiac = "Gemini"
    else:
        zodiac = "Cancer"
elif julian_bday <= 212:
    bmonth = "July"
    bday = julian_bday - 181
    if bday >= 22:
        zodiac = "Cancer"
    else:
        zodiac = "Leo"
elif julian_bday <= 243:
    bmonth = "August"
    bday = julian_bday - 212
    if bday >= 22:
        zodiac = "Leo"
    else:
        zodiac = "Virgo"
elif julian_bday <= 273:
    bmonth = "September"
    bday = julian_bday - 243
    if bday >= 22:
        zodiac = "Virgo"
    else:
        zodiac = "Libra"
elif julian_bday <= 304:
    bmonth = "October"
    bday = julian_bday - 273
    if bday >= 22:
        zodiac = "Libra"
    else:
        zodiac = "Scorpio"
elif julian_bday <= 334:
    bmonth = "November"
    bday = julian_bday - 304
    if bday >= 21:
        zodiac = "Scorpio"
    else:
        zodiac = "Sagittarius"
elif julian_bday <= 365:
    bmonth = "December"
    bday = julian_bday - 334
    if bday >= 21:
        zodiac = "Sagittarius"
    else:
        zodiac = "Capricorn"
# Generate a random birth month and day


def printBirthData():
    print("-------------------------------")
    print("Age:         ", age)
    print("Birth Day:   ", bmonth, "", bday, ", ", birthyear)
    print("Zodiac:      ", zodiac)
    print("-------------------------------")
    __all__ = ['printBirthData']
