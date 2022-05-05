class Area:
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.listDimmensions = [self.height, self.width]

    def findArea(self):
        return self.height * self.width

    def __contains__(self, item):
        if item in self.listDimmensions:
            return True

        return False

    def __delitem__(self, key):
        del self.listDimmensions[key]

    def __getitem__(self, item):
        return self.listDimmensions[item]


def main():
    area1 = Area(15,20)
    area2 = Area(20,30)

    print(15 in area1)
    print(22 in area1)
    print(30 in area2)

    #del area1[1]
    print(area1.listDimmensions[1])

    print(area2[1])

if __name__ == '__main__':
    main()