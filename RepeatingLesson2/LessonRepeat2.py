#Task 1 - First way of Doing
print('\n'
      'task1')

def reverse():
      num=int(input('set 3nums number: '))
      num=str(num)
      num=num[::-1]
      num=int(num)
      print(num)

#reverse()

#Task 1 - Second way of Doing
def mathoper(number):
    a=number // 100 #2
    b=(number // 10) % 10 #23 ->#3
    c=number % 10 #234 % 10 = 4
    print(c,b,a) #432

mathoper(234)


# #Task 1 - Second way of Doing
def mathoper2(number):
     listMy = list(number)
     listMy.reverse()
     nums = listMy[0] + listMy[1] + listMy[3]
     nums = int(nums)

     return nums


#Task 2
print('\n'
      'task2')
def tripplemultyple(*nums):
      for i in nums:
            i=i*3
            print(i, end="::")

tripplemultyple(1,2,6,8,5,3)

#Task 3
"""
Создать функцию, которая принимает в себя 
в качестве параметра три целых числа, функция 
должна вывести количество положительных и 
количество отрицательных чисел.
"""

def numbers(num1, num2, num3):
    positive =0
    negative = 0
    for i in num1, num2, num3:
        if i>0:
            positive += 1
        else:
            negative +=1
    print(f"Positive numbers: {positive}, negative numbers: {negative}")

#Task 3 - Sec way of doing
def numbers2(num1, num2, num3):
    positive =0
    negative = 0
    listNums = [num1,num2,num3]

    negativeNums = []
    positiveNums = []
    for i in listNums:
        if i > 0:
           negativeNums.append(i)
        else:
           positiveNums.append(i)
    print(f"Positive numbers: {len(negativeNums)}, negative numbers: {len(positiveNums)}")

numbers( 5, -4, -8)
numbers2( 5, -4, -8)

#Task 4
"""
Ваша задача написать функцию, 
которая узнает сколько остается дней до определенной даты. 
Для вызова этой функции вам необходимо передать дату, 
после которой вам должно вернутся значение в днях сколько остается 
времени до этой самой даты.
"""
#Aselya
from datetime import datetime
def vremyao(y,m,d):
    todayNow = datetime.now()
    deadline = datetime(y,m,d)
    return deadline - todayNow


print(vremyao(2022,6,1))

#Tilek
print('\n'
      'task4')
from datetime import *

def checkDayLeft(someDate):
    todayNow = datetime.now()
    datetimeUser = datetime.strptime(someDate, '%d/%m/%Y')
    countdata = datetimeUser - todayNow

    print('Time left until: {0} : {1}'.format(datetimeUser.strftime('%d/%B/%y'), countdata))

#userDate=input('set your important data in fromat d/m/yyyy: ')

#checkDayLeft(userDate)


#Task 5
#Aselya
print('Task 5')
raznica = lambda num1, num2: num2/num1
print(raznica(5, 12))

#Tilek
# n1=int(input('set num1: '))
# n2=int(input('set num2: '))
# mathResultLambda  = lambda n1, n2: n1/n2
# print(mathResultLambda(n1,n2))


#Task 6
print('Task 6')

#Aselya
def mylist(listof):
    for i in listof:
        if i%2 == 0:
            print("четное")
        else:
            print("нечетное")

listof=[5,6,9,8,7,10]
mylist(listof)

def checkEven(n):
    if n%2 == 0:
        return "четное"
    else:
        return "нечетное"


newList = list(map(checkEven, listof))
print(newList)

#Task 7
def listok(n):
    n = n.lower()
    return n

somelist =["HELLO","HOW ARE YOU", "I AM FINE", "THANK YOU"]
newlist = list(map(listok, somelist))
newList2 = list(map(lambda w: w.lower(), somelist))

print(newlist)
print(newList2)

