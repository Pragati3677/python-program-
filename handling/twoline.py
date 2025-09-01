f = open("abc.txt", "w")
f.write("First line in file.\n")
f.write("Second line in file.\n")
f.write("Third line in file.\n")
f.close()
 
f = open("abc.txt", "r")

line1 = f.readline().strip()
line2 = f.readline().strip()

print("First Line:", line1)
print("Second Line:", line2)

f.close()
