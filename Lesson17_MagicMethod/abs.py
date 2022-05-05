from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def getBalance(self):
        pass

class BankA(Bank):
    def __init__(self, summa=100):
        super().__init__()
        self.suMMa=summa
    def getBalance(self):
        print(f"Your balance is {self.suMMa} $")

class BankB(Bank):
    def __init__(self, summa1=150):
        super().__init__()
        self.suMMa1=summa1
    def getBalance(self):
        print(f"Your balance is {self.suMMa1} $")


class BankC(Bank):
    def __init__(self, summa2=200):
        super().__init__()
        self.suMMa2=summa2
    def getBalance(self):
        print(f"Your balance is {self.suMMa2} $")




class Car(ABC):
    def __init__(self, model,color,maxSpeed):
        self.modeL=model
        self.coloR=color
        self.maxSpeeD=maxSpeed


    @abstractmethod
    def brake(self):
        print("Вы жмете педаль тормоза!")

    @abstractmethod
    def gas(self):
        print("Вы жмете педаль газа!")

    @abstractmethod
    def display(self):
        pass

class Sedan(Car):
    def __init__(self, model,color,maxSpeed, numofseat,light):
        super().__init__(model, color, maxSpeed)
        self.seatnumber = numofseat
        self.light = light

    def brake(self):
        if self.light == "red" or self.light == "orange":
            print("You should stop the car!")
        else:
            print("Keep going!")

    def gas(self):
        if self.light  == "green":
            print("Keep going!")
        else:
            print("You should stop the car!")

    def display(self):
        print(f"Your car model is {self.modeL}"
              f"\nColor of your car {self.coloR}"
              f"\nMax speed of your car {self.maxSpeeD}"
              f"\nColor of traffic light {self.light}")


class SportCar(Car):
    def __init__(self, model, color, maxSpeed, numofseat1,light):
        super().__init__(model, color, maxSpeed)
        self.seatnumber1 = numofseat1
        self.light = light

    def brake(self):
        if self.light  == "red":
            print("You should stop the car!")

    def gas(self):
        if self.light  == "green":
            print("Keep going!")
        elif self.light  == "orange":
            print("Hurry up, you can pass the traffic light")


    def display(self):
        print(f"Your car model is {self.modeL}"
              f"\nColor of your car {self.coloR}"
              f"\nMax speed of your car {self.maxSpeeD}"
              f"\nColor of traffic light {self.light}")


class FamilyCar(Car):
    def __init__(self, model, color, maxSpeed, numofseat1, baby, light):
        super().__init__(model, color, maxSpeed)
        self.seatnumber1 = numofseat1
        self.baby = baby
        self.light = light

    def brake(self):
        if (self.light  == "red" or self.light  == "orange") and self.baby == "Yes":
            return "You should stop the car!"

    def gas(self):
        if self.light  == "green" and self.baby == "Yes":
            return "Keep going! Safely, cause you have baby on board!"
        else:
            return "Stop the car!"


    def display(self):
        print(f"Your car model is {self.modeL}"
              f"\nColor of your car {self.coloR}"
              f"\nMax speed of your car {self.maxSpeeD}"
              f"\nYou have baby on board {self.baby}"
              f"\nColor of traffic light {self.light}")


def main():
    ABank=BankA()
    ABank.getBalance()
    BBank=BankB()
    BBank.getBalance()
    CBank=BankC()
    CBank.getBalance()
    mainCar=Sedan("Toyota", "red", 50, 5, "red")
    mainCar.display()
    mainCar.gas()
    mainCar.brake()
    secondcar = FamilyCar("Volkswagen", "white", 100, 7, "Yes", "green")
    secondcar.gas()







if __name__ == '__main__':
        main()