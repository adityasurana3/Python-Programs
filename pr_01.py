class programmer:
    company="Microsoft"
    def data(self,name,adress):
        self.name=name
        self.address=adress
    def get_data(self):
        print(f"name is {self.name} and adrress is {self.address} and works in {self.company}")



Employee1=programmer()
Employee1.data("Aditya","India")
Employee1.get_data()
Employee2=programmer()
Employee2.data("Ram","Nepal")
Employee2.get_data()