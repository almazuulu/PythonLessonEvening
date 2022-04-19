class BankAccount:
    def __init__(self, account, balance):
        self.accountPerson = account
        self.balancePerson = balance

    def display(self):
        pass

    def deposit(self, addingSum):
        pass

class VipAccount(BankAccount):
    def __init__(self, account, balance, room):
        BankAccount.__init__(self, account, balance)
        self.service = room
    def vipserving(self):
        print(f'You will be served the first and in the special room.')
        print(f'You can choose rooms to be served:  ')

        for room in self.service:
            print(f'In room: {room}')

class PremiumAcccount(BankAccount):
    def __init__(self, account, balance, numDiscount):
        BankAccount.__init__(self, account, balance)
        self.privilage = numDiscount
    def privilages(self):
        print(f'You have 25% discount. A reserve discount for you 10%. You can use the discount '
        f'{self.privilage} times in a month')

def main():
    acc1=VipAccount(1121, 2000, [23,4,54,5,65,23])
    acc2=PremiumAcccount(1122, 3500, 5)
    acc1.vipserving()
    acc2.privilages()

if __name__=='__main__':
    main()