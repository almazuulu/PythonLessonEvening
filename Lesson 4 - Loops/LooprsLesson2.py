numberCheck = 5
start = 1
factNumber3 = 1

while True:
    factNumber3 = factNumber3 * start
    start += 1
    if start > numberCheck:
        break

print(factNumber3)

count = 0
while True:
    print('Hello Aselya')
    endedOrNot = input('Выходим из цикла? :')

    if endedOrNot == 'yes' or endedOrNot == 'y':
        print('Пока!')
        break

