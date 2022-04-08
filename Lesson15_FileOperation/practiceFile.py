"""
3. Создайте программу, в котором будет записывать введенный
пользователем массив строк (Линию строк) и считывать его обратно из файла на консоль.
"""

fileName = "message.txt"

messagesList = list()

for i in range(4):
    message = input(f'Введите строку {(i+1)}: ')
    messagesList.append(message + "\n")

with open(fileName, 'w') as file:
    for message in messagesList:
        file.write(message)

with open(fileName,'r') as file2:
    content = file2.read()

print(content)



