class Teacher:
    def __init__(self, name, workyears, predmet, numberofstud):
        self.__name=name
        self.__yearswork= workyears
        self.__predmet=predmet
        self.__studnumber=numberofstud

    def displayInfo(self):
        print(f"ФИО учителя: {self.__name}"
              f"\nСтаж учителя: {self.__yearswork}"
              f"\nПредмет, который ведет учитель: {self.__predmet}"
              f"\nКоличество студентов: {self.__studnumber}")

class PhysichTeacher(Teacher):
    def __init__(self, name, workyears, predmet, numberofstud):
        Teacher.__init__(self,name, workyears, predmet, numberofstud)

class ChemistryTeacher(Teacher):
    def __init__(self, name, workyears, predmet, numberofstud):
        Teacher.__init__(self,name, workyears, predmet, numberofstud)

class MathTeacher(Teacher):
    def __init__(self, name, workyears, predmet, numberofstud, num_1, num_2, num_3):
        Teacher.__init__(self,name, workyears, predmet, numberofstud)
        self.num1 = num_1
        self.num2 = num_2
        self.num3 = num_3

    def findAvg(self):
        return (self.num1+self.num2+self.num3)/3

    def display(self):
        super().displayInfo()
        print(f"Среднее значение трех чисел равно {self.findAvg():.2f}")

class GeographyTeacher(Teacher):
    def __init__(self, name, workyears, predmet, numberofstud, namecountry):
        Teacher.__init__(self,name, workyears, predmet, numberofstud)
        self.nameofcountry = namecountry

    def findCapitalcity(self):
        super().displayInfo()
        capitalcity = None
        if self.nameofcountry == "Zimbvabwe":
            capitalcity = "Harare"
            print(f"Для страны {self.nameofcountry} столицей является {capitalcity}")
        else:
            print(f"Вы ввели неправильное название столицы {self.nameofcountry}")



class DrawingTeacher(Teacher):
    def __init__(self, name, workyears, predmet, numberofstud, figuregeometric):
        Teacher.__init__(self,name, workyears, predmet, numberofstud)
        self.geometricfigure = figuregeometric

    def findSimilarObject(self):
        super().displayInfo()
        if self.geometricfigure == "circle":
            print(f"Мячик имеет круглую форму")
        elif self.geometricfigure == "triangle":
            print(f"Пирамида в Египте имеет форму треугольника")
        elif self.geometricfigure == "square":
            print(f"Игральные кости имеет квадратную форму")

class MathGeographyTeacher(MathTeacher, GeographyTeacher):
    def __init__(self, name, workyears, predmet, numberofstud, num_1, num_2, num_3, figuregeometric):
        super().__init__(name, workyears, predmet, numberofstud,num_1, num_2, num_3)
        GeographyTeacher.__init__(self,name, workyears, predmet, numberofstud,figuregeometric)
        super().displayInfo()

    def introducing(self):
        print(f"Hello im math and geo teacher!")

    def display(self):
        super().displayInfo() # не знаю как отразить с двух класов




def main():
    # teacher1 = MathTeacher("Adilet", 15, "Math" , 6, 5, 5, 6)
    # teacher1.findAvg()
    # teacher1.display()
    # teacher2=DrawingTeacher("Altynai", 8, "Draw pictures", 9, "circle")
    # teacher2.findSimilarObject()
    teacheruni=MathGeographyTeacher("Adilet", 7, "MathandGeo", 8, 5,5,6, "circle")
    teacheruni.findAvg()
    teacheruni.introducing()



if __name__=='__main__':
    main()
