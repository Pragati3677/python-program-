class Add:
    def add(self,a,b):
        return a+b
    
    def add(self,a,b,c):
        return a+b+c

a = Add()
# print("addition of two argumnet is",a.add(10,20))
print("Addition of three variables is ",a.add(10,20,30))
