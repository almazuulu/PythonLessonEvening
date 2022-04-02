#raise - создание собственных исключений

result2 = None
try:
    num1 = int(input('Number1: '))
    num2 = int(input('Number2: '))

    if num1 <= 0:
        #print('Вы пытаетесь делить на ноль!')
        raise Exception(' Число должно быть больше нуля!')

    elif num2 <= 0:
        #print('Вы пытаетесь делить на ноль!')
        raise Exception('Вы пытаетесь делить на  число меньше нуля!')

    result2 = num1 // num2

except ZeroDivisionError as ze:
    print('Пытаетесь делить на ноль')
except Exception as e:
    print(f'Ошибка. Тип ошибки: {e}')
finally:
    print(result2)