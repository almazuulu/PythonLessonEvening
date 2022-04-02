def addNums(*nums):
    result = 0

    for i in nums:
        result += i

    return result

def sayHello(n):
    print(f'Hey {n} Hello!')

def main():
    print(addNums(23,43,45,45,65))
    print(addNums(23,23,45,45,65,123,3,45,5,65))

    sayHello('Tilek')
    sayHello('Egor')

if __name__ == '__main__':
    main()
    sayHello('Rinat')