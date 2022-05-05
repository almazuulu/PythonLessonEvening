class Some:

    def __init__(self, name, number2, *args):
        self.name = name
        self.number = number2
        self.myList = list(args)

    def __delitem__(self, key):
        self.myList.remove(key)

    def __del__(self):
        print(f'Object {self.myList} was successfully delete')

        print(f'Deleted {self.myList} object from a class')

    def __lshift__(self, other):
        self.number = self.number << other #1000 -> 2
        return self.number

    def __rshift__(self, other):
        self.number = self.number >> other #1000 -> 2
        return self.number



def main():
    a = Some('Oscar',8,43,54,65)

    print(a>>1)



if __name__=='__main__':
    main()






