number1 = 10
number2 = 15
number3 = 5
number4 = 10

#По умолчанию используется (AND)
#Сравнение - большее меньше
print(number1 > number2) #False
print(number1 < number2) #True

print(number2 > number1) #True
print(number2 < number1) #False

#Сравнение - больше либо равно //  меньше либо равно
print(number1 >= number2) #False
print(number1 <= number2) #True

#Cравнение - равнозначность (==)
print(number1 >= number4) #True
print(number1 <= number4) #True

print(number1 == number4) #True
print(number1 == number2) #False

number1 = 10
number2 = 15
number3 = 5
number4 = 10

#Сравнение на неравнозначность (!=)
print(number1 != number3) #True
print(number2 != number4) #True
print(number1 != number4) #False

#Сложное сравнение True и False
#(True and True) and False = False
print(number1 > number3 < number2 < number4) #False

checkTrue = True
checkFalse = False

#Сравнение на AND выражение
print(checkTrue and checkFalse) #False
print(checkTrue and checkTrue) #True
print(checkFalse and checkFalse)#False

#Сравнение на OR выражение
print(checkTrue or checkFalse) #True
print(checkFalse or checkFalse) #False

#Сравнение на NOT
print(checkTrue != checkTrue) #False
print(checkFalse != checkTrue) #True
print(checkFalse != checkFalse) #False

#Сравнение строковых выражений
letter1 = 'a'
letter2 = 'b'
letter3 = 'A'
letter4 = 'B'

name1 = 'adilet'
name2 = 'Adilet'
name3 = 'ADILET'

print(letter1 < letter2) #True
print(letter1 < letter3) #False
print(letter4 < letter3) #False

print(name1 > name2) #True
print(name2 < name3)








