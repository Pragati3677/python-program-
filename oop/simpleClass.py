class Student:
    def setDetails(self):
        self.name = input("Enter Name:")
        self.roll_no = int(input("Enter roll number:"))


    def display(self):
        print("Name:", self.name)
        print("Roll no:", self.roll_no)


s1 = Student()
s1.setDetails()
s1.display()


