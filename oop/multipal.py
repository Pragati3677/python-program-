# # without constructor
# class A:
#     def a(self):
#         return "i am class A"
# class B():
#     def b(self):
#         return "i am class B"
# class C(A,B):
#     def c(self):
#         return "i am class C"
    
# c1 = C()
# print(c1.a())
# print(c1.b())
# print(c1.c())



# with constructor
# class A:
#     def __init__(self, a_name):
#         self.a_name = a_name

#     def get_a_name(self):
#         print("A name is:", self.a_name)
# class B:
#     def __init__(self, b_name):
#         self.b_name = b_name

#     def get_b_name(self):
#         print("B name is:", self.b_name)
# class C(A, B):
#     def __init__(self, a_name, b_name, c_name):
#         A.__init__(self,a_name) 
      
#         B.__init__(self,b_name)  
     
#         self.c_name = c_name

#     def get_c_name(self):
#         print("C name is:", self.c_name)

# cl = C("Class A", "Class B", "Class C")
# cl.get_a_name()
# cl.get_b_name()
# cl.get_c_name()
