"""
Задание 3
Программа проверки людей на допуск людей
участвовать в голосовании в зависимости от возраста.
"""

votersDict = {"Denis":32, "Sergei":15, "Elena":18, "Timur":17, "Oleg": 27}

keysList = list(votersDict.keys())
valueList = votersDict.values()

allItems = votersDict.items()

print(keysList[1])

for name, age in votersDict.items():
    if age >= 18:
        print(f'Уважаемый, {name}, ваш возраст {age} подходит для голосования!')
    else:
        print(f'Уважаемый, {name}, ваш возраст {age} НЕ подходит для голосования!')


myList = [12,43,54]
#
# number1 = myList[0]
# number2 = myList[1]
# number3 = myList[2]

number1, number2, number3 = myList
print(number2)

print(allItems)

tupleUserInfo = ('Denis', 32)
name, age = tupleUserInfo

print(name)
print(age)
