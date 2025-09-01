# f1 = open("abc.txt", "w")
# f1.write("Hello, this is abc file.\n")
# f1.write("I am writing some content here.\n")
# f1.close()

# f1 = open("abc.txt", "r")
# data = f1.read()
# f1.close()

# f2 = open("pqr.txt", "a")   
# f2.write(data)
# f2.close()

# seek function start from 0
# f2 = open("pqr.txt", "r")
# f2.seek(0)   
# print("Content of pqr.txt:\n")
# print(f2.read())
# f2.close()


# first 10 bytes tell function 
# f1 = open("abc.txt", "w")
# f1.write("Hello, this is abc file.\n")
# f1.write("I am writing some content here.\n")
# f1.close()


# f1 = open("abc.txt", "r")
# data = f1.read(10)   
# print("First 10 bytes:", data)
# print("Current pointer position:", f1.tell())  
