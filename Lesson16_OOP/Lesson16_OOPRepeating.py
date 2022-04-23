class Xerocopy:
    def __init__(self,nameModel, nameDoc, copyQuantity, copyLimit = 20):
        self.nameModel = nameModel
        self.nameDoc  = nameDoc
        self.copyQuantity = copyQuantity
        self.copyLimit = copyLimit

    def addPage(self):
        pageQuant = int(input('Новое количество страниц: '))
        self.copyLimit +=pageQuant

    def Copying(self):
        
        if self.copyQuantity < self.copyLimit:
            print(f'Модель {self.copyQuantity} скопировал документ «{self.nameDoc}» '
              f'в количестве {self.copyQuantity}, осталось {self.copyLimit} листов')

        else:
            print('Не удалось скопировать ваш документ! Добавьте страницы!')
            self.addPage()



class LGTech(Xerocopy):
    pass

def main():
    copy1 = Xerocopy('Xerocopy Samssung1', 'MyFile.txt',20, 25)

    copy1.Copying()

if __name__=='__main__':
    main()