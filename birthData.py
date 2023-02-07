# Zodiac and birthdates
import random

age = random.randint(1, 100)
birthyear = 0
bday = 0
birthyear = 623 - age
zodiac = random.randint(1, 13)

bdate = random.randint(1, 365)
if bdate >= 1 and bdate <= 20:
    zodiac = 1
    bday = random.randint(1, 20)
elif bdate >= 21 and bdate <= 50:
    zodiac = 2
    bday = random.randint(21, 50)
elif bdate >= 51 and bdate <= 80:
    zodiac = 2
    bday = random.randint(51, 80)
elif bdate >= 81 and bdate <= 110:
    zodiac = 3
    bday = random.randint(81, 110)
elif bdate >= 111 and bdate <= 140:
    zodiac = 3
    bday = random.randint(111, 140)
elif bdate >= 141 and bdate <= 170:
    zodiac = 4
    bday = random.randint(141, 170)
elif bdate >= 171 and bdate <= 200:
    zodiac = 4
    bday = random.randint(171, 200)
elif bdate >= 201 and bdate <= 230:
    zodiac = 8
    bday = random.randint(201, 230)
elif bdate >= 231 and bdate <= 260:
    zodiac
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
    birthday = "January" + random.randint(1, 20)
elif zodiac == 2:
    zodiacSign = "Aquarius"
    birthday = "February" + random.randint(1, 20)
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


def BirthData():
    print("-------------------------------")
    print("Age: ", age)
    print("Birth Day: ", bday, ", ", birthyear)
    print("Zodiac: ", zodiacSign)
    print("-------------------------------")
    __all__ = ['BirthData']
