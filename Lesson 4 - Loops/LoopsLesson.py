poem = """
    У лукоморья дуб зелёный;
    Златая цепь на дубе том:
    И днём и ночью кот учёный
    Всё ходит по цепи кругом
"""

text = 'Hello World'

counter = 1

while counter <= 10:
    print(f'Мы повторяем наш стих {counter} раз \n {poem}')
    counter += 1
    #counter = counter + 1

day = 1
destination = 10

while destination <= 20:
    day += 1 #day = day + 1
    destination = destination + 0.1 * destination
    print(f'Бегун пробежал {destination} Количество дней: {day}')

counter = 1

while counter <= 10:
    print(counter ** 2, end=" ")
    counter += 1
    #counter = counter + 1
#
# i = 2
# i *= 10 #i = i * 10
# print(i)

# i = 10
# i -= 1 #i = i - 1
# print(i)


number = int(input('Введите число до которой необходимо вычислить сумму значений: '))

counter = 1
totalSum = 0
while counter <= number:
    totalSum = totalSum + counter
    #total += counter
    counter += 1

print(totalSum)

#Факториал числа 3 = 1*2*3 = 6
#Факториал числа 4 = 1*2*3*4 = 24
#!5 = 1*2*3*4*5 = 120

numb = int(input('Введите число для факториала: '))
counter = 1
factNumber = 1

while counter <= numb:
    factNumber = factNumber * counter
    counter += 1

print(factNumber)

#range(10) 0-9
#range(15,25) 15 - 24
#range(20,30,2) 20 -29 #20, 22, 24, 26, 28


"""
while counter <= 10:
    print(f'Мы повторяем наш стих {counter} раз \n {poem}')
    counter += 1
    #counter = counter + 1
"""

for counter in range(1,11):
    print(f'Мы повторяем наш стих {counter} раз \n {poem}')



"""
numb = int(input('Введите число для факториала: '))
counter = 1
factNumber = 1
while counter <= numb:
    factNumber = factNumber * counter
    counter += 1

print(factNumber)
"""
numb = int(input('Введите число для факториала: '))

factNumber2 = 1
for counter in range(1, numb+1): #range(1,5) 1-4
    factNumber2 = factNumber2 * counter
    print(counter)
print(factNumber2)


k = 0 # начальное значение счетчика while n=>0: # пока число>0 повторять:


#do - while
numberCheck = 5
start = 1
factNumber3 = 1

while True:

    factNumber3 = factNumber3 *  start

    start += 1
    if start == numberCheck + 1:
        break

print(f'Fact number with break:  {factNumber3}')

print('\n')
#[::-1]
#range(1,10) #1-9
#range(10,0,-1)
for i in range(30,19,-1):
    print(i, end=" ")

print('\n')
counter = 30

while counter >= 20:
    print(counter, end=" ")
    counter = counter - 1


