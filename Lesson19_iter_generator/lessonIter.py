listWorkers = ['Aisuluu Osmonova', 'Adilet Shermatov',
               'Cholpon Nazarova', 'Sergei Dolin',
               'Anton Grishin']

# number = 23
# #iterOjb2 = iter(number) #error!

for name in listWorkers:
    print(name)

iterObj = iter(listWorkers)
print('*'*20)

print(listWorkers)
print(iterObj)

print(next(iterObj))
print(next(iterObj))
print(next(iterObj))
print(next(iterObj))
print(next(iterObj))
# print(next(iterObj))

def my_gen():
    for name in listWorkers:
        yield name

print('*'*20)
print(my_gen())

for i in my_gen():
    print(i)


text = "Я учу программирование"

def my_generator():
    for letter in text:
        yield letter

for counter, i in enumerate(my_generator(),1):
    print(f'{counter}-ая буква: "{i}"')











