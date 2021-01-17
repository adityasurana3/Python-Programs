import math
class calculator:
    def __init__(self,num):
        self.number=num
    def square(self):
        print(f"The square of {self.number} is {self.number**2}")

    def sq_root(self):
        
        print(f"The square root of {self.number} is {self.number**0.5}")
    def cube(self):
        print(f"The cube of {self.number} is {self.number**3}")


num = int(input("Enter the number"))
a= calculator(num)
a.square()
a.sq_root()
a.cube()



        