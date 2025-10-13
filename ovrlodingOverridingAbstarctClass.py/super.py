class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def details(self):
        print("Employee name",self.name)
        print("Employee salary",self.salary)

class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department
    def details(self):
        super().details()
        print("department is",self.department)

m = manager("Pargati",56000,"IT")
m.details()