#Множества - set()
#Создание множеств set

mySet1 = {}
mySet2 = set()

print(mySet1)
print(mySet2)

print(type(mySet1))
print(type(mySet2))

#Создание множеств с реальными данными
setNumbers = {12,34,56,67,12,34,56,11,13}
setString = {'Alexei','Igor', 'Murat', 'Nurzhan', 'Murat', 'Igor'}
mixedSet = {12,3.45, 12, 'Hello', 'c', 12, 'Hello'}

print(setNumbers)
print(setString)
print(mixedSet)

listNumb = list(range(15,30,3))
print(listNumb)

listNumb.append(15)
listNumb.append(21)
listNumb.append(15)
listNumb.append(18)

print(listNumb)
setFromList = set(listNumb)
print(setFromList)

myListDoctors = ['Oleg', 'Timur', 'Asan', 'Oleg', 'Timur', 'Aisulu']
myListDoctors = list(set(myListDoctors))

print(myListDoctors)

#Свойства множества
#Операция удаления со множества

setNumbers = {12,34,56,67,12,34,56,11,13}
setString = {'Alexei','Igor', 'Murat', 'Nurzhan', 'Murat', 'Igor'}
mixedSet = {12,3.45, 12, 'Hello', 'c', 12, 'Hello'}

#print(setString)
#setString.pop()
print(setString)

setString.remove('Igor')
print(setString)

setString.discard('Murat')
print(setString)

#Добавление новых элементов
setString.add('Samara')
setString.add('Adilet')
setString.add('Oleg')

print(setString)
print('Adilet' not in setString)

#intersection(), "&" -  Для выявление общих элементов

hospital1 = {'Igor', 'Elena', 'Aisulu', 'Samat', 'Stepan'}
hospital2 = {'David','Sergei','Elena', 'Samat', 'Timur'}

sameWorkers = hospital1.intersection(hospital2)
print(hospital1.intersection(hospital2))
print(sameWorkers)

sameWorkers2 = hospital1 & hospital2
print(hospital1 & hospital2)
print(sameWorkers2)


#difference(), "-" - Выявление уникальных элементов м-у двумя множествами
print(hospital1.difference(hospital2))
print(hospital2.difference(hospital1))

print(hospital1 - hospital2)
print(hospital2 - hospital1)

uniqueWorkersH1 = hospital1.difference(hospital2)
print(uniqueWorkersH1)

#union(), "|" - Объединение двух множеств
hospital1 = {'Igor', 'Elena', 'Aisulu', 'Samat', 'Stepan'}
hospital2 = {'David','Sergei','Elena', 'Samat', 'Timur'}

twoHospital = hospital1.union(hospital2)
print(twoHospital)

twoHospital2 = hospital1|hospital2
print(twoHospital2)

myListDoctors = ['Oleg', 'Timur', 'Asan', 'Oleg', 'Timur', 'Aisulu']

hospital2 = {'David','Sergei','Elena', 'Samat', 'Timur'}
hospital2.update(myListDoctors)
print(hospital2)


for doctor in hospital2:
    print(doctor)

weeks = frozenset({'Monday', 'Tuesday', 'Wednesday'})
print(weeks)


twoHospital = hospital1.union(hospital2)
print(twoHospital)
hospital1.update(hospital2)

print(hospital1)

