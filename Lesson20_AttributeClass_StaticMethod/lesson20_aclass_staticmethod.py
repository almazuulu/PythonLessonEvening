class Person:
    type = "Person"
    description = "Этот класс описывает поведение человека"
    default_name = "Askar"
    id = 0

    salary = 10000
    sumSalary = 0

    @staticmethod
    def incrementing_id():
        Person.id += 1

        for i in range(Person.id):
            Person.sumSalary+= Person.salary

        print(Person.sumSalary)
        #return Person.id

    @staticmethod
    def displaySum():
        total_salary = None
        for i in range(Person.id):
            pass
        return total_salary
    def __init__(self, name):
        # self.name = name
        if name:
            self.name = name
        else:
            self.name = Person.default_name

        self.id_person = "id_worker_" + str(self.name)
        #self.id_person  = id


    def display(self):
        print(self.name)

    @staticmethod
    def print_typeClass():
        print(Person.type)
        print(Person.description)

p1 = Person("")
print(p1.type)
p1.type = "Handsome Person"
print(p1.type)

print(p1.name)

p2 = Person("Oleg")
print(p2.name)

p2.display()

print(Person.id)

p3 = Person("")
print(Person.id)

print(p1.id_person)
print(p2.id_person)
print(p3.id_person)

p10 = Person("")
print(p10.id_person)

Person.incrementing_id()
print(p1.salary)
print(p2.salary)



myDict = {
    'p1': 10000,
    'p2': 10000,
    'p3':10000
}

total_salary = 0
for i,salary in myDict.items():
    total_salary += salary

print(total_salary)

