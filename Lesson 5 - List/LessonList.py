#Создание списка
from copy import deepcopy
myList = []
myList2 = list()

print(myList)
print(myList2)

print(type(myList))
print(type(myList2))

#Создание и придание значение к спискам
myListNumber = [23,43,5,76,11,56]
myListNames = ['Aisuluu', 'Olga', 'Timur', 'Esen', 'Mariya', 'Asan']
mixedList = [12, 'Hello', 4.56, 's', False, 45,123]

print(myListNumber)
print(myListNames)
print(mixedList)

myListNumber2 = list(myListNumber)
print(myListNumber2)

myListNumber3 = myListNumber2
print(myListNumber3)

print(myListNumber3 == myListNumber2)
myListNumber[2] = 45
print(f'myListNumber1: {myListNumber}')
print(f'myListNumber2: {myListNumber2}')
print(f'myListNumber3: {myListNumber3}')

myListNumber2[4] = 17
print(f'myListNumber1: {myListNumber}')
print(f'myListNumber2: {myListNumber2}')
print(f'myListNumber3: {myListNumber3}')

myListNumber4 = myListNumber2.copy()
myListNumber2[3] = 100
print(f'myListNumber1: {myListNumber}')
print(f'myListNumber2: {myListNumber2}')
print(f'myListNumber3: {myListNumber3}')
print(f'myListNumber4: {myListNumber4}')

#Создание списка с одинаковыми элементами
myListNumberSix = [6] * 10
print(myListNumberSix)

myListNumberSame = myListNumber * 4
print(myListNumberSame)

#Расширение списка extend
myListNumber5 = [100,23,77,65,11,33,44]
print(myListNumber5)
myListNumber5.extend(myListNumber)
print(myListNumber5)


#Создание списка с помощью range()
#range(start,finish,step)
#range(4,20) - 4 - 19
#range(4,20,3) - 4, 7, 10, 13, 16, 19

myListNumberRange = list(range(10)) #0-9
print(myListNumberRange)

myListNumberRange2 = list(range(10, 51, 10)) #10,20,30,40
print(myListNumberRange2)

#100 - 20 - 10
myListRangeReversed = list(range(100,19,-10))
print(myListRangeReversed)


myListNumber = [23,43,5,76,11,56]
#1-ое число: 23
#2-ое число: 43 ..

#Перебор списка и операции с помощью циклов
#for
print('===Цикл For====')
count = 1
for number in myListNumber:
    print(f'{count}-ое число: {number}')
    count += 1

#Циклы
print('===Цикл While====')
counter = 0
while counter < len(myListNumber):
    print(f'{counter + 1}-ое число: {myListNumber[counter]}')
    counter += 1


#Математические  операции с помощью циклов
#for
print('===Цикл For====')
count = 1
for number in myListNumber:
    print(f'{count}-ое число: {number * 3}')
    count += 1

print('===Цикл While====')
counter = 0
while counter < len(myListNumber):
    print(f'{counter + 1}-ое число: {myListNumber[counter] * 3}')
    counter += 1

# Добавление к списку методом append() и insert()
myListNumber = [23,43,5,76,11,56]
myListNames = ['Aisuluu', 'Olga', 'Timur', 'Esen', 'Mariya', 'Asan']
mixedList = [12, 'Hello', 4.56, 's', False, 45,123]

#append()
myListNumber.append(12)
print(myListNumber)

myListNames.append('Sergei')
print(myListNames)

#insert()
myListNumber.insert(1, 67)
print(myListNumber)

myListNames.insert(3,'Murat')
print(myListNames)

#Удаление со списка pop() remove() del

#pop() - удаление с конца
myListNumber.pop()
print(myListNumber)

#pop() - удаление с указанием индекса
myListNumber.pop(2)
print(myListNumber)

#remove()
myListNames.remove('Timur')
print(myListNames)

#del
del myListNames[2]
print(myListNames)

#Очищение списка при помощи clear() del

#clear() - Очищает список, без удаления самого списка или параметра
myListNames.clear()
print(myListNames)

myListNames.append('Alena')
myListNames.append('Sergei')
myListNames.append('Arslan')

print(myListNames)

myListNames = ['Aisuluu', 'Olga', 'Timur', 'Esen', 'Mariya', 'Asan']

#del - Полностью удаляет сам список т.е переменную
print(myListNames)
del myListNames
#print(myListNames)

#index() count()

#index()
myListNames = ['Aisuluu', 'Olga', 'Timur', 'Esen', 'Mariya', 'Asan', 'Olga', 'Esen', 'Olga']
print(myListNames.index('Esen'))

#count - подсчет дубликатов
print(myListNames.count('Olga')) #3
print(myListNames.count('Esen')) #2

#Статистические ф-ии в списке
myListNumber = [23,43,5,76,11,56]

#min() max() sum()

#max()
print(max(myListNumber))

#min()
print(min(myListNumber))

#sum()
print(sum(myListNumber))

#max() - String list
print(max(myListNames))

#min() - String list
print(min(myListNames))

#sum() - String list
#print(sum(myListNames))#Error

#Сортировка списка - sorted() sort() reverse() reversed()

#sorted()
myListNumber = [23,43,5,76,11,56]
print(sorted(myListNumber))
print(myListNumber)

#sort()
myListNumber.sort()
print(myListNumber)

print('====reversed===')
#reversed()
myListNumber = [23,43,5,76,11,56]
myListNumber.sort()
print(myListNumber)
#print(reversed(myListNumber))

# myListNumber77 = reversed(myListNumber)
# print(myListNumber77)
#

myListNumber.reverse()
print(myListNumber) #myListNumber[::-1]

# Срезы списоков
print(myListNumber[:])
print(myListNumber[:3])
print(myListNumber[3:])
print(myListNumber[2:4])
print(myListNumber[::-1])

myListNumber = myListNumber[::-1]
print(myListNumber)
someList = myListNumber[2:4]
print(someList)

del myListNumber[2:5]
print(myListNumber)

listNum1 = [23,43,56,7]
listNum2 = list(range(11,20))

print(listNum1)
print(listNum2)

listNum3 = listNum1 + listNum2
print(listNum3)

listNum1.extend(listNum2)
print(listNum1)

#Вложенный список
myListNested = [
    [123,23,54,65,34],
    [12,3,23,76,7],
    [12,46,11,34,6]
]

print(len(myListNested))
print(myListNested[1])
print(myListNested[1][3])


for numbers in myListNested:
    for number in numbers:
        print(f'Число: {number}')

print(min([123,34,33,4]))
minNumber = min(myListNumber)
print(minNumber)

