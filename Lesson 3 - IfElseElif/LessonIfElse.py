"""
if [True]:
    code
else:
    code
"""

number1 = 10
number2 = 20

# if number1 > number2:
# print('Первое число больше чем второе!')
# else:
# print('Первое число меньше чем второе!')

if number1 > number2:
    print('Первое число больше чем второе!')
else:
    print('Первое число меньше чем второе!')


age = int(input('Введите свой возраст: '))

if age >= 25 and age <= 41:
    print('Вы нам подходите! Мы берем Вас на работу!')
else:
    print('Увы ваш возраст слишком мал либо ваш возраст не лежит в данном отрезке!\n'
          'Мы не можем взять на работу!')

print('\n')
if age >= 25 or age <= 41: #True OR False = True
    print('Вы нам подходите! Мы берем Вас на работу!')
else:
    print('Увы ваш возраст слишком мал либо ваш возраст не лежит в данном отрезке!\n'
          'Мы не можем взять на работу!')


#a  = 3
a  = 15
print(range(10)) #  числа в промежутке 0-9

if a in range(10):
    print('Да лежит в этом промежутке')
else:
    print('Не лежит в этом отрезке!')

# listNum = list(range(10))
# print(listNum)

number1 = 10
number2 = 20
number3 = 30

# #max - min (максимальное значение)
# print(max(number1, number2, number3)) # 30
# print(min(number1, number2, number3)) # 10
#
# number1 = int(input('Пишите число 1: '))
# number2 = int(input('Пишите число 2: '))
# number3 = int(input('Пишите число 3: '))
#
# if max(number1, number2, number3) == number2:
#     print(f'Максимальное значение {number2}')
# else:
#     print(f'Максимальное значение не равно {number2}')


#IF - Else - Else IF
address1 = 'Chuy 1'
address2 = 'Bokonbaeva 23'

addressDostavki = input('Введите адресс доставки: ')

if addressDostavki == 'Chuy 1':
    print('Клиент получил посылку!')
elif addressDostavki == 'Bokonbaeva 23': #Else if
    print('Клиент получил посылку!')
else:
    print('Доставка не доставлена!')

#Сложная конструкция IF-Else-Elif (Nested)
age = int(input('Введите свой возраст для выборов: '))

if age >= 18:
    print('Вы допущены к выборам!')

    if age == 18:
        print('Вы голосуете в первый раз! Вам от нас подарок!')
    elif age >= 100:
        print('Вам достается двойной подарок! Так как вы у нас рекодсмен по голосованию!')
    elif age >= 65 and age <= 99 :
        print('Вы можете голосовать из дома!')
        print('Вы голосуете НЕ в первый раз! Вам НЕТ подарка!')
    else:
        print('Вы голосуете НЕ в первый раз! Вам НЕТ подарка!')

else:
    print('Вы НЕ допущены к выборам!')


"""
if number1 > number2:
    print('Первое число больше чем второе!')
else:
    print('Первое число меньше чем второе!')
"""

number1 = 20
number2 = 10
print('\n')
#Тернарный оператор
# [Code execute == True] if True else [Code execute if code is False]
# [Код сработает если значение true] [if Сравнение]  else [Код сработает если False]
resultText = 'Первое число больше чем второе!' if number1 > number2 else 'Первое число меньше чем второе!'

print(resultText)

numberOper = int(input('Введите для операции 1-Сложение 2-Вычитание'))

