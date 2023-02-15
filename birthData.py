# Zodiac and birthdates
import random
import requests

import getRace

age = 0


def getAge():
    # Age
    if getRace.selected_race == "Dwarf":
        age = random.randint(50, 350)
    elif getRace.selected_race == "Elf":
        age = random.randint(100, 750)
    elif getRace.selected_race == "High-Elf":
        age = random.randint(100, 750)
    elif getRace.selected_race == "Wood-Elf":
        age = random.randint(100, 750)
    elif getRace.selected_race == "Dark-Elf":
        age = random.randint(100, 750)
    elif getRace.selected_race == "Half-Orc":
        age = random.randint(14, 75)
    elif getRace.selected_race == "Halfling":
        age = random.randint(20, 120)
    elif getRace.selected_race == "Human":
        age = random.randint(18, 50)
    elif getRace.selected_race == "Dragonborn":
        age = random.randint(15, 80)
    elif getRace.selected_race == "Gnome":
        age = random.randint(40, 500)
    elif getRace.selected_race == "Half-Elf":
        age = random.randint(20, 120)
    elif getRace.selected_race == "Tiefling":
        age = random.randint(18, 60)
    elif getRace.selected_race == "Goliath":
        age = random.randint(16, 80)
    else:
        age = random.randint(18, 50)

    return age


age = getAge()

birthyear = 0
bday = 0
birthyear = 623 - age
zodiac = random.randint(1, 13)
zodiacSign = ""

bdate = random.randint(1, 365)
if bdate >= 1 and bdate <= 20:
    zodiac = 1
    bday = random.randint(1, 20)
elif bdate >= 21 and bdate <= 50:
    zodiac = 2
    bday = random.randint(21, 50)
elif bdate >= 51 and bdate <= 80:
    zodiac = 3
    bday = random.randint(51, 80)
elif bdate >= 81 and bdate <= 110:
    zodiac = 4
    bday = random.randint(81, 110)
elif bdate >= 111 and bdate <= 140:
    zodiac = 5
    bday = random.randint(111, 140)
elif bdate >= 141 and bdate <= 170:
    zodiac = 6
    bday = random.randint(141, 170)
elif bdate >= 171 and bdate <= 200:
    zodiac = 7
    bday = random.randint(171, 200)
elif bdate >= 201 and bdate <= 230:
    zodiac = 8
    bday = random.randint(201, 230)
elif bdate >= 231 and bdate <= 260:
    zodiac = 9
    bday = random.randint(231, 260)
elif bdate >= 261 and bdate <= 290:
    zodiac = 10
    bday = random.randint(261, 290)
elif bdate >= 291 and bdate <= 320:
    zodiac = 11
    bday = random.randint(291, 320)
elif bdate >= 321 and bdate <= 350:
    zodiac = 12
    bday = random.randint(321, 350)
elif bdate >= 351 and bdate <= 365:
    zodiac = 13
    bday = random.randint(351, 365)

if zodiac == 1:
    zodiacSign = "Capricorn"
    birthday = "January"
elif zodiac == 2:
    zodiacSign = "Aquarius"
    birthday = "February"
elif zodiac == 3:
    zodiacSign = "Pisces"
elif zodiac == 4:
    zodiacSign = "Aries"
elif zodiac == 5:
    zodiacSign = "Taurus"
elif zodiac == 6:
    zodiacSign = "Gemini"
elif zodiac == 7:
    zodiacSign = "Cancer"
elif zodiac == 8:
    zodiacSign = "Leo"
elif zodiac == 9:
    zodiacSign = "Virgo"
elif zodiac == 10:
    zodiacSign = "Libra"
elif zodiac == 11:
    zodiacSign = "Scorpio"
elif zodiac == 12:
    zodiacSign = "Sagittarius"
elif zodiac == 13:
    zodiacSign = "Capricorn"


birthyear = 0
birthyear = 623 - age
zodiacroll = random.randint(1, 24)

if zodiacroll == 1:
    bday = random.randint(22, 31)
    bmonth = "December"
    sign = "Capricorn"
if zodiacroll == 2:
    bday = random.randint(1, 20)
    bmonth = "January"
    sign = "Capricorn"
if zodiacroll == 3:
    bday = random.randint(1, 19)
    bmonth = "February"
    sign = "Aquarius"
if zodiacroll == 4:
    bday = random.randint(20, 29)
    bmonth = "February"
if zodiacroll == 5:
    bday = random.randint(1, 20)
    bmonth = "March"
    sign = "Pisces"
if zodiacroll == 6:     
    bday = random.randint(21, 31)
    bmonth = "March"
    sign = "Aries"
if zodiacroll == 7:
    bday = random.randint(1, 20)
    bmonth = "April"
    sign = "Aries"
if zodiacroll == 8:
    bday = random.randint(21, 30)
    bmonth = "April"
    sign = "Taurus"
if zodiacroll == 9:
    bday = random.randint(1, 21)
    bmonth = "May"
    sign = "Taurus"
if zodiacroll == 10:
    bday = random.randint(22, 31)
    bmonth = "May"
    sign = "Gemini"
if zodiacroll == 11:
    bday = random.randint(1, 21)
    bmonth = "June"
    sign = "Gemini"
if zodiacroll == 12:
    bday = random.randint(22, 30)
    bmonth = "June"
    sign = "Cancer"
if zodiacroll==13:
    bday=random.randint(1,22)
    bmonth = "July"
    sign = "Cancer"
if zodiacroll==14:
    bday=random.randint(23,31)
    bmonth = "July"
    sign = "Leo"
if zodiacroll==15:
    bday=random.randint(1,23)
    bmonth = "August"
    sign = "Leo"
if zodiacroll==16:
    bday=random.randint(24,31)
    bmonth = "August"
    sign = "Virgo"
if zodiacroll==17:
    bday=random.randint(1,23)
    bmonth = "September"
    sign = "Virgo"
if zodiacroll==18:
    bday=random.randint(24,30)
    bmonth = "September"
    sign = "Libra"
if zodiacroll==19:
    bday=random.randint(1,23)
    bmonth = "October"
    sign = "Libra"
if zodiacroll==20:
    bday=random.randint(24,31)
    bmonth = "October"
    sign = "Scorpio"
if zodiacroll==21:
    bday=random.randint(1,22)
    bmonth = "November"
    sign = "Scorpio"
if zodiacroll==22:
    bday=random.randint(23,30)
    bmonth = "November"
    sign = "Sagittarius"
if zodiacroll==23:
    bday=random.randint(1,21)
    bmonth = "December"
    sign = "Sagittarius"
if zodiacroll==24:
    bday=random.randint(22,31)
    bmonth = "December"
    sign = "Capricorn"

def printBirthData():
    print("-------------------------------")
    print("Age:         ", age)
    print("Birth Day:   ", bmonth, "",bday, ", ", birthyear)
    print("Zodiac:      ", sign)
    print("-------------------------------")
    __all__ = ['printBirthData']
    
