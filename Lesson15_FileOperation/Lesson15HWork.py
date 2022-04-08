
from random import choice
"""
2. Напишите программу на Python для подсчета количества
строк в текстовом файле.
"""

counter = 0
with open('someText.txt', 'r') as file:
    line = file.readline()

    while line:
        counter += 1
        line = file.readline()
    print(counter)

"""
3. Напишите программу на Python для чтения случайной строки из файла.    
"""

with open('someText.txt', 'r') as file2:
    listWord = file2.readlines()

print(choice(listWord))
print(listWord[0])











