num = ()
n = input("Enter how many names you want to add: ")
for i in range(int(n)):
    value = input("Enter name: ")
    num.append(value)
print("The tuple is:", num)