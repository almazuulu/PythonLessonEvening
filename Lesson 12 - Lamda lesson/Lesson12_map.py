def powerNum(num):
    return num ** 2

def powerNum2(num):
    numList = []

    for i in num:
        numList.append(i**2)

    return numList

def checkAge(age):
    if age>=18:
        return 'You can vote!'
    else:
        return 'Too young!'

myList = list(range(1,20))
#[1,2,3,4,5,6....]
print(myList)

print(powerNum2(myList))

poweredList = list(map(powerNum,myList))
print(poweredList)

poweredNum = lambda n: n**2

poweredList2 =  list(map(poweredNum, myList))
print(poweredList2)

listAges = [12,45,47,18,24,23,17,19,16]
print(listAges)
checkAgeList = list(map(checkAge, listAges))
print(checkAgeList)

#Task2
def someFunc():
    pass




