#Task 5
"""Создать функцию, которая принимает в
качестве параметра двузначное число,
необходимо найти сумму и произведение его цифр."""


number = input('Put some number: ')

def findSomeNums(num):
    listNum = list(num)
    num1, num2 = listNum
    num1 = int(num1)
    num2 = int(num2)

    resultSum = num1 + num2

    return resultSum

print(f'Сумма двух принятых чисел равно: {findSomeNums(number)}')
