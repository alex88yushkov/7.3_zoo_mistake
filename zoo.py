class Zoo:
    def __init__(self):
        self.animals = {"Squirrel": 2}
        self.employee = ["John"]

    def track(self):
        for key, value in self.animals.items():
            print("Animal : {} , Quantity : {}".format(key, value))
        print("Employee:", ', '.join(map(str, self.employee)))

    def add_animal(self, new_animal):
        x = self.animals.keys()
        t = len(self.employee) * 10
        if new_animal is "":
            self.animals["Squirrel"] = self.animals["Squirrel"] + 1
            print("One squirrel has been added")
        else:
            if new_animal in x:
                if sum(self.animals.values()) < t:
                    self.animals[new_animal] = self.animals[new_animal] + 1
                    print(new_animal, "has been added, total quantity: ", self.animals.get(new_animal))
                else:
                    print("Not enough employees for all animals! Hire someone new!")
            else:
                self.animals[new_animal] = 1
                print(new_animal, "has been added, total quantity: ", self.animals.get(new_animal))

    def del_animal(self, animal):
        x = self.animals.keys()
        if animal in x:
            if self.animals[animal] > 0:
                self.animals[animal] = self.animals[animal] - 1
                print(animal, "has been deleted, total quantity: ", self.animals.get(animal))
            else:
                print("We don't have any", animal, "in our Zoo")
        else:
            print("We don't have any", animal, "in our Zoo")

    def add_employee(self, employee):
        x = self.employee
        x.append(employee)
        print(employee, "has been hired")

    def del_employee(self, employee):
        x = self.employee
        if employee is not "":
            x.remove(employee)
            print(employee, "has been fired")
        else:
            print(self.employee[-1], "has been fired")
            x.pop()


get_zoo = Zoo()
get_zoo.del_employee("")
get_zoo.track()

