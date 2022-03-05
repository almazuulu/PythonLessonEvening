"""
Task 6

Создайте программу, которая удаляет имена рабочих до тех
пор, пока пользователь не пожелает остановиться.
До тех пор, пока пользователь не напишет ‘нет’ с данного
списка рабочих ['Елена', 'Степан', 'Мурат', 'Асан', 'Айсулуу']
должны удаляться имена
"""

myWorkerList = ['Елена', 'Степан', 'Мурат', 'Асан', 'Айсулуу']
command = ' '

print(f'Изначальный список рабочих: {myWorkerList}')
while command != 'нет':
        deleteName = input('Какого рабочего удалить? :')
        myWorkerList.remove(deleteName)

        print(f'Обновленный список рабочих: {myWorkerList}')

        command = input('Желаете продолжить? \n'
                        'Если да нажмите на любую кнопку, '
                        '\nиначе напечатайте "нет": ')

        if command == 'нет':
            print('Программа завершена! Всего доброго!')

print(f'\n Обновленный список после Цикла: {myWorkerList}')

