class Employee:
    def __init__(self, name, salary, subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
    def getDetails(self):
        print(f"name: {self.name}\nsalary: {self.salary}\nsubunit: {self.subunit}")
    


Aditya = Employee("Aditya",100,"Programmer")
Aditya.getDetails()
