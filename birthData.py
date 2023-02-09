# Zodiac and birthdates
import random

age = random.randint(18, 100)
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


def BirthData():
    print("-------------------------------")
    print("Age: ", age)
    print("Birth Day: ", bday, ", ", birthyear)
    print("Zodiac: ", zodiacSign)
    print("-------------------------------")
    __all__ = ['BirthData']


# birthyear=0
# birthyear=623 - age
# zodiacroll=random.randint(1,24)

# if zodiacroll==1:
#     bday=random.randint(22,31)
#     print('Dec,', bday, '- ', birthyear)
#     print('Capricorn')
# if zodiacroll==2:
#     bday=random.randint(1,20)
#     print('Jan', bday, birthyear)
#     print('Capricorn')
# if zodiacroll==3:
#     bday=random.randint(21,31)
#     print('Jan', bday, birthyear)
#     print('Aquarious')
# if zodiacroll==4:
#     bday=random.randint(1,18)
#     print('Feb', bday, birthyear)
#     print('Aquarious')
# if zodiacroll==5:
#     bday=random.randint(19,29)
#     print('Feb', bday, birthyear)
#     print('Picies')
# if zodiacroll==6:
#     bday=random.randint(1,19)
#     print('Mar', bday, birthyear)
#     print('Picies')
# if zodiacroll==7:
#     bday=random.randint(20,31)
#     print('Mar', bday, birthyear)
#     print('Aries')
# if zodiacroll==8:
#     bday=random.randint(1,19)
#     print('Apr', bday, birthyear)
#     print('Aries')
# if zodiacroll==9:
#     bday=random.randint(20,30)
#     print('Apr', bday, birthyear)
#     print('Taurus')
# if zodiacroll==10:
#     bday=random.randint(1,20)
#     print('May', bday, birthyear)
#     print('Taurus')
# if zodiacroll==11:
#     bday=random.randint(21,31)
#     print('May', bday, birthyear)
#     print('Gemini')
# if zodiacroll==12:
#     bday=random.randint(1,20)
#     print('Jun', bday, birthyear)
#     print('Gemini')
# if zodiacroll==13:
#     bday=random.randint(21,30)
#     print('Jun', bday, birthyear)
#     print('Cancer')
# if zodiacroll==14:
#     bday=random.randint(1,22)
#     print('Jul', bday, birthyear)
#     print('Cancer')
# if zodiacroll==15:
#     bday=random.randint(23,31)
#     print('Jul', bday, birthyear)
#     print('Leo')
# if zodiacroll==16:
#     bday=random.randint(1,22)
#     print('Aug', bday, birthyear)
#     print('Leo')
# if zodiacroll==17:
#     bday=random.randint(23,31)
#     print('Aug', bday, birthyear)
#     print('Virgo')
# if zodiacroll==18:
#     bday=random.randint(1,22)
#     print('Sep', bday, birthyear)
#     print('Virgo')
# if zodiacroll==19:
#     bday=random.randint(23,30)
#     print('Sep', bday, birthyear)
#     print('Libra')
# if zodiacroll==20:
#     bday=random.randint(1,21)
#     print('Oct', bday, birthyear)
#     print('Libra')
# if zodiacroll==21:
#     bday=random.randint(22,31)
#     print('Oct', bday, birthyear)
#     print('Scorpio')
# if zodiacroll==22:
#     bday=random.randint(1,21)
#     print('Nov', bday, birthyear)
#     print('Scorpio')
# if zodiacroll==23:
#     bday=random.randint(22,31)
#     print('Nov', bday, birthyear)
#     print('Sagittarious')
# if zodiacroll==24:
#     bday=random.randint(1,21)
#     print('Dec', bday, birthyear)
#     print('Sagittarious')