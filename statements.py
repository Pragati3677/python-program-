#1 write a Python program that reads a value of n and check the number is zero or non zero value
num = int(input('Enter the number:'))
if num>0:
   print('non-zero number')
else:
    print('zero number')    


#2 write a Python program to find a largest of tw numbers
num1 = int(input('Enter the frist number:'))
num2 = int(input('Enter the second number:'))
if num1>num2:
    print('num1 is large')
else:
    print('num2 is large')    

#3. write a python program that reads the number and check the number is positive or negative
num1 = int(input('Enter the frist number:'))
if num1>0:
    print('num1 is positive')
else:
    print('num2 is negative')   
    

#4. write a pythone program to check character is vowel or consonant
vowel = input('Enter the character:')
if vowel in 'aeiouAEIOU':
    print('vowel')
else:
    print('consonant')


#5 write a python program to evalute the student performance
marks = int(input('Enter the marks:'))
if marks >= 90:
    print('Excellent performance')
elif marks >= 80:
    print('very Good performance') 
elif marks >= 70:
    print('Good performance')
elif marks >= 60:
    print('Average performance')
else:
    print('Poor performance')
           

#6 Write the pythone progaram to find largest of three numbers
num1 = int(input('Enter the frist number:'))
num2 = int(input('Enter the second number:'))
num3 = int(input('Enter the third number:'))
if num1>num2 and num1>num3:
     print('num1 is large')
elif num2>num1 and num2>num3:
    print('num2 is large')  
elif num3>num1 and num3>num2:
     print('num3 is large')      


#7 write a program to find the smallest of three numbers
num1 = int(input('Enter the frist number:'))
num2 = int(input('Enter the second number:'))
num3 = int(input('Enter the third number:'))
if num1<num2 and num1<num3:
    print('num1 is small')
if num2<num1 and num2<num3:
    print('num2 is small')
if num3<num1 and num3<num2:
    print('num3 is small')        