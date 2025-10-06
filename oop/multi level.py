# multi level inheritance
# without constructor


# class grandparent:
#     def grnd(self):
#         return "i am grandparent"
    
# class parent(grandparent):
#     def par(self):
#         return "i am parent"

# class child(parent):
#     def chi(self):
#         return "i am child"
    
# c1 = child()
# print(c1.grnd())
# print(c1.par())
# print(c1.chi())


# with constructor
class Grandparent:
    def __init__(self, gp_name):
        self.gp_name = gp_name

    def get_gp_name(self):
        print("Grandparent name is:", self.gp_name)
class parent(Grandparent):
    def __init__(self, gp_name, p_name):
        super().__init__(gp_name)  
        self.p_name = p_name

    def get_p_name(self):
        print("Parent name is:", self.p_name)

class child(parent):
    def __init__(self, gp_name, p_name, c_name):
        super().__init__(gp_name, p_name)  
        self.c_name = c_name

    def get_c_name(self):
        print("Child name is:", self.c_name)

cl = child("lakshman", "shantilal", "Pragati")
cl.get_gp_name()
cl.get_p_name()
cl.get_c_name()

