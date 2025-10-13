class employee:
    def show_details(self,name):
        print("Name is",self.name)
    def show_details(self,name,sername):
        print("Name is",name)
        print("Sername is",sername)
    
e = employee()
# e.show_details("Pragati")
e.show_details("Pragati","Shendage")

# class Employee:
#     def show_details(self, name, salary=None):
#         print(f"Name:",name)
#         if salary is not None:
#             print(f"Salary:",salary)
#         print()

# e = Employee()
# e.show_details("Pragati")           
# e.show_details("Pragati", 50000)    
