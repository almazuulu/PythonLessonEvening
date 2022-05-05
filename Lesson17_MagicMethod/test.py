class Area:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def __str__(self):
        return f'{self.__height}'

    def __call__(self, *args, **kwargs):
        return self.__width * self.__height

    # def figureArea(self):
    #     area = self.__width * self.__height
    #     return area

    # def __gt__(self, other):
    #     # if isinstance(other, Area) < isinstance(self, Area):
    #     #     return print(f'Figure 1 is less then Figure 2')
    #     # elif isinstance(other, Area) < isinstance(self, (int, float)):
    #     #     return print(f'Figure 1 is greater then Figure 2')
    #     # else:
    #     #     return print(f'Сравниваем 2 числа')
    #     #
    #
    #     if isinstance(other, Area):
    #         otherarea = other.figureArea()
    #         ownarea = self.figureArea()
    #
    #         if ownarea > otherarea:
    #             return True
    #         else:
    #             return False
    #
    #     else:
    #         ownarea = self.figureArea()
    #
    #         if ownarea > other:
    #             return True
    #         else:
    #             return False
    #
    # def __lt__(self, other):
    #     # if isinstance(other, Area) < isinstance(self, Area):
    #     #     return print(f'Figure 1 is less then Figure 2')
    #     # elif isinstance(other, Area) < isinstance(self, (int, float)):
    #     #     return print(f'Figure 1 is greater then Figure 2')
    #     # else:
    #     #     return print(f'Сравниваем 2 числа')
    #     #
    #
    #     if isinstance(other, Area):
    #         otherarea = other.figureArea()
    #         ownarea = self.figureArea()
    #
    #         if ownarea < otherarea:
    #             return True
    #         else:
    #             return False
    #
    #     else:
    #         ownarea = self.figureArea()
    #
    #         if ownarea < other:
    #             return True
    #         else:
    #             return False





are1  = Area(12,14) #168
are2  = Area(15,12) #180

# print(are1 > are2) #False
#
# print(are1 > 12) #False
#
# print(are1 < are2) #True
#
# print(are1 < 12) #False
# print(12 < are1) #False

a1 = are1()
a2 = are2()

print(are1())
print(are2())
print(are1)





