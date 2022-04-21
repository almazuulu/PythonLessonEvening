class Teacher:
    def __init__(self, name, quantStudent, subject, experience):
        self.__name = name
        self.quantStudent = quantStudent
        self.__subject = subject
        self.experience = experience

    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName

    def setSubject(self, newSubject):
        self.__subject = newSubject

    def display(self):
        print(f'Name of the teacher: {self.__name}'
              f'\nQuant student: {self.quantStudent}'
              f'\nSubject name: {self.__subject}'
              f'\nExperience: {self.experience}')

class Person:
    def __init__(self,agePerson):
        self.agePerson =  agePerson


class MathTeacher(Teacher, Person):
    def __init__(self,name, quantStudent, subject, experience, n1,n2,n3, agePerson):
        super().__init__(name, quantStudent, subject, experience)
        Person.__init__(self,agePerson)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def findAvg(self):
        return (self.n1 + self.n2 + self.n3)/3

    def display(self):
        super().display()
        print(f'Avarage is: {self.findAvg()}')


class GeographyTeacher(Teacher):
    def __init__(self, name, quantStudent, subject, experience,nameOfCountry):
        Teacher.__init__(self,name, quantStudent, subject, experience)
        self.nameOfCountry = nameOfCountry

    def findCityOfCountry(self):

        capitalCity = ' '
        if self.nameOfCountry == 'Turkey':
            capitalCity = 'Istanbul'

        elif self.nameOfCountry == 'Germany':
            capitalCity = 'Berlin'

        elif self.nameOfCountry == 'Sweden':
            capitalCity = 'Vienna'

        return capitalCity

    def display(self):
        super().display()
        print(f'Capital of {self.nameOfCountry} is {self.findCityOfCountry()}')

class MathAndGeoTeahcher(MathTeacher, GeographyTeacher):
    def __init__(self,name, quantStudent, subject, experience, n1,n2,n3, nameOfCountry):
        MathTeacher.__init__(self,name, quantStudent, subject, experience, n1,n2,n3)
        GeographyTeacher.__init__(self,name, quantStudent, subject, experience,nameOfCountry)

    def display(self):
        MathTeacher.display(self)
        GeographyTeacher.display(self)

    def greeting(self):
        print(f'I am Math and Geo teacher!')

def main():
    teacher1 = MathTeacher('Valentin Sergeev',45,'Algebra',12, 45, 56, 45,65)
    teacher2 = GeographyTeacher('Oleg Valerievich', 51, 'Geography', 7, 'Germany')
    # teacher3  = MathAndGeoTeahcher('Talant Kadyrbekov',32,'Geometry and Geography',
    #                                15, 23, 45, 67,'Turkey')

    teacher1.display()
    print('*'* 10)
    teacher2.display()
    print('*' * 10)

    print(f'Average is: {teacher1.findAvg()}')
    print(f'Capital is: {teacher2.findCityOfCountry()}')

    print(MathTeacher.mro())
    # teacher3.display()

if __name__ == '__main__':
    main()








