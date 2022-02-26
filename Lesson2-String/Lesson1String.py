text = 'Some text'
text = 'Some word2' #0-9 - 10
print(text)

print(text[1]) #o
print(text[0]) #S
print(text[5])
print(len(text)) #длина слова сост 10 букв

numb = 12
numb1 = str(numb)
print(type(numb))
print(type(numb1))

print('Я живу в Кыргысзтане.\nВ городе Бишкек и работаю тут же')
print('Я живу в Кыргысзтане.\tВ городе Бишкек и работаю тут же')

"""
Какой-нибудь комментарий. 
Эти кавычки могут служить для отображение текста в желаемой
нами структуре
"""

poem = """
    У лукоморья дуб зелёный;
    Златая цепь на дубе том:
    И днём и ночью кот учёный
    Всё ходит по цепи кругом
"""

print(poem)

info = "Я живу в Кыргысзтане.\nВ городе Бишкек и работаю тут же"

if 'виж' in info:
    print('Этот город есть в данном тексте')

if 'Мос' not in info:
    print('Данного города нет в этом тексте')

#Срезы
word = 'Python Programming'

print(word[1:]) #ython Programming
print(word[0:6]) #Python
print(word[7:]) #Programming

langProgramming = word[0:6]
subject = word[7:]
print(langProgramming)
print(subject)

#вывод текста в обратном направлении
print(word[::-1]) #gnimmargorP nohtyP
print(word[-4:-1]) #min

#Py Programming
word2 = word[0:2] + ' ' + word[7:]
print(word2)

word = 'Python Programming'
#Шаги в срезах
#[start:stop:step]
print(word[0:7:2]) #Pto
print(word[0:12:3]) #Ph o
print(word[0]=='P') #True
print(word[0]=='T') #False

print(word[17])

print(word.find('Programming')) #7
print(word.find('Test')) #-1 слово не найдено
print(word.find('ming')) #находится в 14 индексе

word2 = 'Programming'
print(word2.rfind('m'))
print(word2.find('m'))

progLang2 = word.replace('Python', 'Java')
print(progLang2)

someWord = 'Hello Sellingll'
someWord2 = someWord.replace('l', 'P', 5) #HePPo SePPingPL
print(someWord2)

#function count()
print(someWord.count('l')) #6

info = 'I live in Bishkek. My parents also live in Bishkek. ' \
       'In Bishkek we have a lot flowers. Bishkek is a very nice city'

wordS = 'Test'

print(info.count('Bishkek'))
print(wordS[1::])


#Строковые методы представления
someText = 'i live in paris'
print(someText.upper())
someText2 = someText.upper() #I LIVE IN PARIS
someText3 = someText2.lower() #i live in paris
someText4 = someText3.capitalize() #I live in paris

fileName = 'homework.pdf'
fileName2 = 'homework.doc'

if fileName2.endswith('.pdf'):
    print('Принимаю вашу Домашку!')
else:
    print('Переделай файл!')

fileSend = 'practice.pdf'
fileSend2 = 'lessonPractice.pdf'

if fileSend2.startswith('practice'):
    print('Принимаю вашу Практику!')
else:
    print('Переделай файл!')

fileSize = '1024'
fileSize2 = 'O'
print(fileSize.isdigit()) #True
print(fileSize2.isalpha())
print(someText3.islower())


testWord = '        Some beatiful world      '
print(testWord)

testWord_RemoveLeft = testWord.lstrip() #Some beatiful world....
print(testWord.lstrip())

testWord_RemoveRight = testWord.rstrip() #   Some beatiful world|
print(testWord.rstrip())

testWord_RemoveBothSide = testWord.strip()
print(testWord_RemoveBothSide)

testWord2 = '$$$word$$$'
testWord3 = '@@@word$$$'
testWordRemoveSignLeft = testWord2.lstrip('$')#word$$$
print(testWordRemoveSignLeft)

testWordRemoveSignRight = testWord2.rstrip('$')#$$$word
print(testWordRemoveSignRight)

testWordRemoveSignBoth = testWord2.strip('$')
print(testWordRemoveSignBoth)#word

testWordRemLeft2 = testWord3.lstrip('@') #word$$$
print(testWordRemLeft2)

testWordRemLeft2 = testWord3.strip('@') #word$$$
print(testWordRemLeft2)

name = 'Askar'
city = 'Bishkek'
age = 30
address = 'Mira 7'

print('Имя: ', name, 'city: ',city, 'Age: ', age )

#Format method displaying
print('Имя: {0} city: {1} Возраст: {2} Адресс: {3}'.format(name,city,age,address))

print('Поезд отправляется в {0}! Повторяю! Поезд отправляется в {0} '
      'Человек по имени {1} поторопитесь!'.format(address,name))

print('Поезд отправляется в {addr}! Повторяю! Поезд отправляется в {addr} '
      'Человек по имени {fullname} поторопитесь!'.format(addr = address,fullname = name))

#Отображение с помощью F-string
print(f'Имя: {name}\ncity: {city}\nВозраст: {age}\nАдресс: {address}')



