name = "Askar"
name2 = "Tilek"

number = 24
myList = [23,4,54,6,67]

name = name.lower()
name2 = name2.upper()
print(type(name))
print(type(name2))
print(name)
print(name2)

print(id(name))
print(id(name2))

print(type(number))
print(type(myList))

myList.pop()
print(myList)

# class Person:
#     name = 'Askar'
#     age = 25
#
# person1 = Person()
# person2 = Person()
#
# print(type(person1))
# print(type(person2))
#
# print(person1.name)
# print(person2.name)


class Auto:
    # brandName = 'Toyota'
    # modelName = 'Camry'
    # engine = '2.4'
    # color = 'White'

    # brandName = None
    # modelName = None
    # engine = None
    # color = None

    def __init__(self, brandName,modelName,engine,color ):
        self.nameBrand = brandName
        self.nameModel = modelName
        self.carEngine = engine
        self.carColor = color

        #print('Объект создан, и все значения приняты!')

    def displayMainInfo(self):
        print(f'Brand name: {self.nameBrand}')
        print(f'Model name: {self.nameModel}')
        print(f'Color of the car: {self.carColor}')
        print(f'Engine of the car: {self.carEngine}')

    def nameBrandCapital(self):
        self.nameBrand = self.nameBrand.upper()

car1 = Auto('Toyota', 'LC200', '2.4', 'White')
car2 = Auto('Lexus', 'GX470', '3.2', 'Yellow')
car3 = Auto('BMW', '525', '3.2', 'Silver')
car4 = Auto('Aston Marting', '5', '3.0', 'Brown')
car5 = Auto('Audi', 'A8', '2.6', 'Black')

# car3.modelName = 'BMW 525'
# car3.color = 'Red'
# car5.color = 'Blue'
#
# car3.engine = '3.0'

# print(car1.modelName)
# print(car1.color)
# print(car1.engine)
#
# print(car3.modelName)
# print(car3.color)
# print(car3.engine)
#
# print(car5.modelName)
# print(car5.color)
# print(car5.engine)

car1.displayMainInfo()
car2.displayMainInfo()
car3.displayMainInfo()
car5.displayMainInfo()

car1.nameBrandCapital()
car1.displayMainInfo()

car5.nameBrandCapital()
car5.displayMainInfo()
print(car5.nameBrand)

car6 = Auto('Jiguli', '7','1.8','white')


# car1.modelName = 'BMW 7'
# car1.color = 'White'
# car1.engine = '1.8'
#
# car2.modelName = 'Audi A8'
# car2.color = 'Yellow'
# car2.engine = '2.4'

class AirConditioner:
    def __init__(self, modelName, temp):
        self.nameModel = modelName
        self.temperature = temp

    def turnOff(self):
        self.temperature = None
        print(f'Air conditioner {self.nameModel} is turned OFF!'
              f'and\nits Temperature is: {self.temperature}!')

    def turnOn(self):
        self.temperature = 20
        print(f'Air conditioner {self.nameModel} is turned ON '
              f'and\nits Temperature is: {self.temperature}!')

    def setNewTemp(self, new_temperature):
        self.temperature = new_temperature

        print(f'You canged Air Cond {self.nameModel} to new Temperature'
              f'and\nits new Temperature is: {self.temperature}!')

    def seeInfo(self):
        print(f'Model Name: {self.nameModel}')
        print(f'Current Temp: {self.temperature}')

    def makeHot(self):
        self.temperature = 35
        print(f'Air Cond {self.nameModel} is set to HOT Mode and its new Temperature'
              f'\n is: {self.temperature}!')

airCond_1 = AirConditioner('LG Cond Ux5423', 16)
airCond_2 = AirConditioner('Samsung CoolAir 72', 18)
airCond_3 = AirConditioner('Beko Sweet 55', 25)

airCond_1.seeInfo()
airCond_2.seeInfo()
airCond_3.seeInfo()

airCond_2.turnOff()

airCond_1.seeInfo()
airCond_2.seeInfo()
airCond_3.seeInfo()

airCond_1.makeHot()

airCond_1.seeInfo()
airCond_2.seeInfo()
airCond_3.seeInfo()

airCond_2.turnOn()

airCond_1.seeInfo()
airCond_2.seeInfo()
airCond_3.seeInfo()

# Пример Кофе
class CoffeeMachine:
    def __init__(self, namemodel, quantOfMilk, quantofwater, quantCoffee):
        self.modelName = namemodel
        self.qMilk = quantOfMilk
        self.qWater = quantofwater
        self.qCoffee = quantCoffee

        if self.qMilk < 0:
            self.qMilk = 0

    def makeLatte(self):
        milkQuantlatte = 200
        waterqantLatte = 250
        coffelatte = 2
        if self.qMilk <= 0 or self.qWater <= 0 or self.qCoffee <=0:
            print(f'Добавьте пожалуйста ингридиенты! '
                  f'Кол-во воды, кофе или молока не достаточно!')

            print('Не удалось приготовить Латте!')
        else:
            self.qMilk = self.qMilk - milkQuantlatte
            self.qWater -= waterqantLatte
            self.qCoffee -= coffelatte

            print('Ваше Латте готово!')

    def makeCappucino(self):
        milkQuantCappucino = 100
        waterqantCappucino = 300
        coffeCappucino = 4

        if self.qMilk <= 0 or self.qWater <= 0 or self.qCoffee <=0:
            print(f'Добавьте пожалуйста ингридиенты! '
                  f'Кол-во воды, кофе или молока не достаточно!')

            print('Не удалось приготовить Каппучино!')
        else:
            self.qMilk = self.qMilk - milkQuantCappucino
            self.qWater -= waterqantCappucino
            self.qCoffee -= coffeCappucino

            print('Ваше Каппучино готово!')

    def displayInfo(self):
        print(f'Milk :{self.qMilk}'
              f'\nWater: {self.qWater}'
              f'\nCoffe: {self.qCoffee}')

    def addIngridients(self, newquantMilk, newquantWater, newquantCoffee):
        self.qMilk = self.qMilk + newquantMilk
        self.qWater += newquantWater
        self.qCoffee += newquantCoffee

        print('Новое количество: ')
        self.displayInfo()

#Кофемашине в отделе Экономических расход
coffeMachine1 = CoffeeMachine('Samsung', 1000, 1000, 10)
coffeMachine1.makeLatte()
coffeMachine1.makeCappucino()
coffeMachine1.makeCappucino()
coffeMachine1.makeCappucino()
coffeMachine1.makeCappucino()

coffeMachine1.displayInfo()

coffeMachine1.addIngridients(0, 500, 5)
coffeMachine1.makeCappucino()

coffeMachine1.displayInfo()

#Кофемашине в отделе Экономических доходов
coffeMachine2 = CoffeeMachine('LG', 2000, 2000, 20)
coffeMachine2.makeLatte()
coffeMachine2.makeCappucino()
coffeMachine2.makeCappucino()
coffeMachine2.makeCappucino()
coffeMachine2.makeCappucino()

coffeMachine2.displayInfo()

# coffeMachine1.qCoffee = 12
# coffeMachine1.qMilk = 23
# coffeMachine1.qWater = 1000

#Кофемашине в отделе Планирование расходов
coffeMachine3 = CoffeeMachine('Samsung', -100, 2000, 20)
coffeMachine3.displayInfo()

print(coffeMachine3.modelName)
coffeMachine3.modelName = 'Indesit'
print(coffeMachine3.modelName)

name = 'Someone'
age = 12

