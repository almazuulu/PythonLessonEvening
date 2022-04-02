try:
    age = int(input('Введите ваш возраст: '))
    print(f'Возраст: {age}')

except:
    print('Произошла ошибка!')

# age = int(input('Введите ваш возраст: '))
# print(f'Возраст: {age}')
# print('Code....')

result = None

try:
    num1 = int(input('Number1: '))
    num2 = int(input('Number2: '))

    result = num1 // num2

except ZeroDivisionError:
    print('Вы пытались делить на ноль!')
except ValueError:
    print('Ошибка. Введите цифровое значение!')
except:
    print('Ошибка!')
finally:
    print(f'Результат: {result}')

print('Code....')

peopleList = ['Aselya', 'Tilek', 'Nikolai', 'Sergei', 'Alena']

result2 = None
try:
    num1 = int(input('Number1: '))
    num2 = int(input('Number2: '))

    result2 = num1 // num2

    print(peopleList[7])

except IndexError as ie:
    print(f'Вы вышли за пределы массива! {ie}')
except ZeroDivisionError as ze:
    print(f'Вы пытались делить на ноль! {ze}')

    # num1 = int(input('Number1: '))
    # num2 = int(input('Number2: '))
    #
    # result = num1 // num2
except ValueError as ve:
    print('Введите число!')

except BaseException as be:
    print(f'Ошибка! Тип ошибки: {be}')

finally:
    print(f'Результат: {result2}')

print('Code....')