# without constructor

class Person:
    def info(self):
        print("I am a person")


class Employee(Person):
    def employee(self):
        print("I am an employee")

class WorkingPersoon(Employee, Person):
    def working_student(self):
        print("I am a working Person")


w = WorkingPersoon()
w.info()             
w.employee()        
w.working_student() 
