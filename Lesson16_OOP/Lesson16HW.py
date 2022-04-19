#Practice task 2
class Person:
    def __init__(self, name, adress, age=18):
        self.__namePerson = name
        self.__agePerson = age
        self.__adressPerson = adress
        self.__can_vote = None

        # if self.__agePerson >= 18:
        #     self.__can_vote = 'yes, can vote'
        # else:
        #     self.__can_vote = 'cannot vote'

        if self.__agePerson >= 18:
            self.__can_vote = True
        else:
            self.__can_vote = False

    def getpersonName(self):
        return self.__namePerson

    def setName(self, newname):
        self.__namePerson= newname

    def getAge(self):
        return self.__agePerson

    def setAge(self, newage):
        self.__agePerson = newage
         
        # if self.__agePerson >= 18:
        #     self.__can_vote = 'yes, can vote'
        # else:
        #     self.__can_vote = 'cannot vote'
        if self.__agePerson >= 18:
            self.__can_vote = True
        else:
            self.__can_vote = False

    def displayInfo(self):
        if self.__can_vote == True:
            print(f'Name: {self.__namePerson}'
                  f'\nAge person: {self.__agePerson}'
                  f'\nAddress person: {self.__adressPerson}'
                  f'\nCan vote? :Может голосовать')
        else:
            print(f'{self.__namePerson} Вы не допущены к голосованию! ')

def main():
    person1 = Person('Adilet', 'Mira 7', 25 )
    person2 = Person('Samat', 'Tolstoy 12', 23)
    person3 = Person('Sergei','Moscow str 77',32)

    person3.setAge(13)

    person1.displayInfo()
    person2.displayInfo()
    person3.displayInfo()


if __name__=='__main__':
    main()








