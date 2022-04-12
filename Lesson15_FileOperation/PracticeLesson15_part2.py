from openpyxl import *

"""
2.  Отобразите все уникальные название городов, 
категорий, регионов из файла ‘food.xlsx’
"""
def showUniqueData(filename, sheet):


    #unique regions
    region = sheet['B']
    regionList = [r.value for r in region if r.value!='Region']

    regionList = list(set(regionList))
    print(f'Уникальные регионы из файла: {regionList}')

    # unique cities
    cities = sheet['C']
    cityList = [c.value for c in cities if c.value!='City']

    cityList = list(set(cityList))
    print(f'Уникальные города из файла: {cityList}')

    # unique categories
    categories = sheet['D']
    categoriesList = [categ.value for categ in categories if categ.value != 'Category']

    categoriesList = list(set(categoriesList))
    print(f'Уникальные Категории из файла: {categoriesList}')


"""
3.  
a) Создайте страницу ‘marks’

b) Создайте следующие заголовки:
• Имя школьника
• Математика
• География
• Астрономия
• Химия
• Физика

c) Примите от пользователя количество учеников, которых необходимо добавить в данный файл, 
путем цикла примите данные для этих учеников и заполните исходя из заголовка задания b)

d) Используя формулу запишите в отдельные поля:
• Итоговая оценка (Всех учеников)
• Средняя оценка (Для всех учеников)
"""

def taskThree(filename, sheet, wb):

    headersList  = ['ФИО', 'Математика', 'География','Астрономия','Химия',
                    'Физика', 'Среднее значение','Cумма']
    dataStudents = list()
    #=AVERAGE(B2:F2)
    #=SUM(B2:F2)

    #quantChild = int(input('Введите кол-во учеников для записи: '))

    quantChild = int(input('Кол-во учеников'))

    for i in range(quantChild):
        name = input('Имя ученика: ')
        math = int(input('Оценка по Математике: '))
        geography = int(input('Оценка по Географии: '))
        astronomy = int(input('Оценка по Астрономии: '))
        chemistry = int(input('Оценка по Химии: '))
        physics = int(input('Оценка по Физике: '))

        dataStudents.append((name,math,geography,astronomy,chemistry,physics))

    dataStudents.insert(0,tuple(headersList))
    #print(dataStudents)
    dataStudents = tuple(dataStudents)

    for data in dataStudents:
        sheet.append(data)

    counter = 2
    for i in range(quantChild):
        sheet['H'+str(counter)] = f'=SUM(B{counter}:F{counter})'
        sheet[f'G{counter}'] = f'=AVERAGE(B{counter}:F{counter})'
        counter += 1

    # sheet['H1'] = 'Total'
    # sheet['H2'] = '=SUM(B2:F2)'
    # sheet['H3'] = '=SUM(B3:F3)'
    # sheet['H4'] = '=SUM(B4:F4)'
    #
    # sheet['G1'] = 'Average'
    # sheet['G2'] = '=AVERAGE(B2:F2)'
    # sheet['G3'] = '=AVERAGE(B3:F3)'
    # sheet['G4'] = '=AVERAGE(B4:F4)'

    wb.save(filename)


def main():
    filename = 'food.xlsx'

    wb = load_workbook(filename)
    sheet = wb.worksheets[0]
    sheet2 = wb.create_sheet('marks')

    showUniqueData(filename, sheet)
    taskThree(filename, sheet2, wb)


if __name__ == '__main__':
    main()




