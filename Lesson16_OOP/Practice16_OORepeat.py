class Xerocopy:
    def __init__(self, nameModel, nameDoc, copyQuantity, copyLimitPage):
        self.__Modelname = nameModel
        self.__Docname = nameDoc
        self.__Quantitycopy = copyQuantity
        self.__Limitcopypage = copyLimitPage

    def Copy(self):
        pagenum=int(input("Введите количество страниц для копирования: "))
        #ostatoklistov = 0
        if self.__Limitcopypage < pagenum or self.__Limitcopypage <= 0:
            print("Не осталось листов в копировальном аппарате!")

        else:
            self.__Limitcopypage = self.__Limitcopypage - pagenum
            print(f"Модель {self.__Modelname} скопировал документ {self.__Docname} в количестве {pagenum}, осталось {self.__Limitcopypage} листов")

        #self.__Limitcopypage = ostatoklistov

    def addList(self):
        pagenum1 = int(input("Введите количество страниц для добавления: "))

        oldPage = self.__Limitcopypage
        if self.__Limitcopypage < 0:
            pass
        else:
            self.__Limitcopypage = self.__Limitcopypage + pagenum1

        print(f"У вас на копировальном аппарате было {oldPage}, после пополнения стало {self.__Limitcopypage} листов.")

class Printer:
    def __init__(self, nameModel, nameDoc, copyQuantity, copyLimitPage):
        self.__Modelname1 = nameModel
        self.__Docname1 = nameDoc
        self.__Quantitycopy1 = copyQuantity
        self.__Limitcopypage1 = copyLimitPage

    def Printing(self):
        pagenum = int(input("Введите количество страниц для печатание: "))
        # ostatoklistov = 0
        if self.__Limitcopypage1 < pagenum or self.__Limitcopypage1 <= 0:
            print("Не осталось листов в копировальном аппарате!")

        else:
            self.__Limitcopypage1 = self.__Limitcopypage1 - pagenum
            print(
                f"Модель {self.__Modelname1} распечатал документ {self.__Docname1} в количестве {pagenum}, осталось {self.__Limitcopypage1} листов")

        # self.__Limitcopypage = ostatoklistov

    def addList(self):
        pagenum1 = int(input("Введите количество страниц для добавления: "))

        oldPage = self.__Limitcopypage1
        if self.__Limitcopypage1 < 0:
            pass
        else:
            self.__Limitcopypage1 = self.__Limitcopypage1 + pagenum1

        print(f"У вас на копировальном аппарате было {oldPage}, после пополнения стало {self.__Limitcopypage1} листов.")


class LGTech(Xerocopy,Printer):
    def __init__(self,nameModel, nameDoc, copyQuantity, copyLimitPage):
        super().__init__(nameModel, nameDoc, copyQuantity, copyLimitPage)
        Printer.__init__(self,nameModel, nameDoc, copyQuantity, copyLimitPage)


def main():
    # printer1 = Xerocopy("Xerox", "Referat", 15, 30)
    # printer1.Copy()
    # printer1.addList()

    lg1 = LGTech("Xerox", "Referat", 15, 30)

    lg1.Printing()


if __name__=='__main__':
    main()