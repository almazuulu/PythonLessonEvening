# name = input("Введите ваше имя: ")
# age = int(input("Введите ваш возраст: "))
# address = input("Введите ваш адрес проживания: ")
#
# print(name)
# print(age)
# print(address)
#
# print(f"Имя: {name} , возраст: {age}, адрес проживания: {address}")
# print("Имя: {0} , возраст: {1}, адрес проживания: {2}".format(name, age, address))
# print("Имя: {0} , возраст: {1},{0}, адрес проживания: {2},{0}".format(name, age, address))
# print("Имя: {name} , возраст: {age}, адрес проживания: {adress}".format(name=name,age= age,adress= address))

# #Срезы
# print(name[1])
# print(name[1:])

progLang = 'Python Language'

print(progLang[7:])
print(progLang.lstrip('Python '))
print(progLang[:7:3])
print(progLang[0:7:3])
print(progLang[::-1])

#Методы String
if 'Language' not in progLang:
    print('This word does not exists in Prog Lang')
else:
    print('This word exists in Prog Lang')

city = 'Bishkek' #Bi

if city.startswith('Bi'):
    print('Yes')

if city.endswith('kek'):
    print('Yes')

word = '$$$$hello$$$$'

print(word.lstrip('$'))
print(word.rstrip('$'))
print(word.strip('$'))

word2 = '$$$$hello%%%%'
print(word2.strip('$%'))
print(word2.lstrip('$').rstrip('%'))

word3 = 'i am learnin python'
print(word3.upper())

word4 = word3.upper()
print(word4)
print(word4.lower())
print(word4.capitalize())

word3 = word3.replace('python','java')
print(word3)

"""
tenet = tenet
довод = довод

принимаем слово от пользователя и необходимо проверить принятое слово,
действительно или оно зеркальное

Пример:
Аскар = раксА - не зеркальное!
довод = довод - зеркальное!

Если слово зеркальное --> "Ваше слово зеркальное"
Иначе --> "Оно не зеркальное"
"""

numberList = [123,[324,54,2,4],34,11,[13,54,2,[4354,3,[12,4,54,6]]]]

print(numberList[2]) #34
print(numberList[1][1]) #54
print(numberList[4][2]) #2
print(numberList[4][3][1])
print(numberList[4][3])
print(numberList[4][3][1]) #3
print(numberList[4][3][2][3])

tupleNum = (123,43,54,2)

print(sorted(tupleNum))
print(tupleNum)

mySet = {234,54,65,23,5,54,23,5,5,5,23}
print(mySet)

myListNum = [234,35,645,21,34,12,21,12,35,234]
myListNum = list(set(myListNum))
print(myListNum)

mySet1 = {34,54,23,43,65,87}
mySet2 = {43,23,54,34,11,65,77}

print(mySet1.intersection(mySet2))
print(mySet1.difference(mySet2))

mySet3 = mySet1.union(mySet2)
print(mySet3)






