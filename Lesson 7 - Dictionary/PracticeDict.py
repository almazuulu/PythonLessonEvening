"""
Task 1
Создайте программу, в которой пользователь будет
указывать размер словаря, после чего устанавливать
ключи и значения с клавиатуры.
"""
myDict = dict()
lenOfDict = int(input('Введите размер вашего словаря: '))

for i in range(lenOfDict):
    keyOfDict = input('Введите ключ: ')
    valueOfDict = input('Введите значние: ')

    myDict[keyOfDict] = valueOfDict

print(myDict)


