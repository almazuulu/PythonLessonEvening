#Кортежи - tuple()
#Создание кортежей tuple()

myTuple = ()
myTuple2 = tuple()

print(myTuple)
print(myTuple2)

print(type(myTuple))
print(type(myTuple2))

myTupleNumber = (12,4,34,23,11)
myStringTuple = ('Hello', 'Work', 'Mariya', 'World')
mixedTuple = (12,3,56.34, 'Hello', 12, 's')

print(myTupleNumber)
print(myStringTuple)
print(mixedTuple)

listNumb = list(range(1,10))
print(listNumb)

myNumberTuple2 = tuple(listNumb)
print(myNumberTuple2)
print(type(myNumberTuple2))

print(myStringTuple[1])
print(mixedTuple[-3])

print(mixedTuple[0:4])
print(mixedTuple[:4])


myTupleNumber = (12,4,34,23,11)
myStringTuple = ('Hello', 'Work', 'Mariya', 'World')
mixedTuple = (12,3,56.34, 'Hello', 12, 's')

helloWord = myStringTuple[0]
work = myStringTuple[1]
nameMariya = myStringTuple[2]
world = myStringTuple[3]

print(helloWord)
print(work)
print(nameMariya)
print(world)

print('\n')

helloWord2, work2, nameMariya2, world2 = myStringTuple
print(helloWord2)
print(work2)
print(nameMariya2)
print(world2)

myList = [23,4,5,576]
numb1, numb2, numb3, numb4 = myList

print(numb1)
print(numb2)
print(numb3)
print(numb4)

myTupleNumber = (12,4,34,23,11)
myStringTuple = ('Hello', 'Work', 'Mariya', 'World', 'World', 'World')
mixedTuple = (12,3,56.34, 'Hello', 12, 's')

print(max(myTupleNumber))
print(min(myTupleNumber))
print(sum(myTupleNumber))
print(sorted(myTupleNumber))

sampleNumb = sorted(myTupleNumber)
print(type(sampleNumb))

for word in myStringTuple:
    print(word, end=" ")

count = 0

print('\n')
while count<len(myStringTuple):
    print(myStringTuple[count], end=" ")
    count += 1

myTupleNested = (
            (12,3,23),
            (23,43,54,6)
            )
print('\n')
for row in myTupleNested:
    for num in row:
        print(num, end=" ")
    print(end="\n")

word = 'something'
myTupleWord = tuple(word)
print(myTupleWord)





