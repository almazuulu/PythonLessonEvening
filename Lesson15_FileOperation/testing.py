from openpyxl import *
wb = open('food.xlsx', data_only=True)
sheet = wb.worksheets[0]

cells = sheet['A14': 'G25']
region = sheet['B']


"""
06.02.2020	East	Boston	Crackers	Whole Wheat	28	3,49
09.02.2020	West	Los Angeles	Bars	Carrot	44	1,77
12.02.2020	East	New York	Bars	Carrot	23	1,77
15.02.2020	East	New York	Snacks	Potato Chips	27	1,35
18.02.2020	East	Boston	Cookies	Arrowroot	43	2,18
21.02.2020	East	Boston	Cookies	Oatmeal Raisin	123	2,84
24.02.2020	West	Los Angeles	Bars	Bran	42	1,87
27.02.2020	West	Los Angeles	Cookies	Oatmeal Raisin	33	2,84
02.03.2020	East	New York	Cookies	Chocolate Chip	85	1,87
05.03.2020	West	San Diego	Cookies	Oatmeal Raisin	30	2,84
08.03.2020	East	Boston	Bars	Carrot	61	1,77
11.03.2020	East	Boston	Crackers	Whole Wheat	40	3,49
"""
dataList = [[cell.value for cell in list(row)] for row in cells]
#print(dataList)
counter = 0
print(dataList)
for i in dataList:
    for data in i:
        if data in ('Boston','Los Angeles') :
            continue
        print(data, end=" ")
    print(end="\n")
    counter+=1

#unqie list of regions
region = sheet['B']
regionList = [r.value for r in region[1:]]
regionList = list(set(regionList))
print(regionList)

#unqie list of cities

cities = sheet['C']
citiesList = [c.value for c in cities[1:]]
citiesList = list(set(citiesList))
print(citiesList)



