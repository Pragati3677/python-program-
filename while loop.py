# 1 write a program to print natural numbers upto n
# n = int(input('Enter the value of n: '))
# i = 1
# while i<=n:
#     print(i)
#     i +=1


# 2 write a program to print even numbers up to n
# n = int(input('Enter the value of n: '))
# i=2
# while i<=n:
#     print(i)
#     i += 2


# 3 write a pythone program to print odd numbers up to n
# n = int(input('Enter the value of n: '))
# i = 1
# while i<=n:
#     print(i)
#     i+=2

# 4 Write a pythone program to print sum of natural numbers
# n = int(input('Enter the value of n: '))
# i = 1
# sum = 0
# while i<=n:
#     sum += i
#     i+=1
# print(sum)


# 5 Write a python program to print sum of odd numbers upto n
# n = int(input('Enter the value of n: '))
# sum = 0
# i = 1
# while i<=n:
#     sum +=i
#     i+=2
# print(sum)


# 6 Write a program to print a sum of even numbers upto n
# n = int(input('Enter the value of n: '))
# sum = 0
# i = 2
# while i<=n:
#     sum += i
#     i+=2
# print(sum)

# 7 write a program to print the natural numbers upto n in reverse order
# n = int(input('Enter the value of n: '))
# while n>=1:
#     print(n)
#     n-=1    

# 8 Write a program to print the fibonaccci series up to n
# n = int(input('Enter the value of n: '))
# a,b = 0,1
# count = 0
# print('fibonacci series')
# while count<n:
#     print(a,end=' ')
#     next_term = a+b
#     a=b
#     b=next_term
#     count += 1
# print()


# 9 write a program to find a factorial of given number
# n = int(input('Enter the value of n:'))
# factorial = 1
# i = 1
# while i<=n:
#     factorial *= i
#     i+=1
# print(factorial)

# 10 write a program to check whether the given number is prime or not
# n= int(input('Enter the number:'))
# is_prime = True
# i = 2
# while i*i <= n:
#     if n % i == 0:
#         is_prime = False
#         break
#     i += 1
# if is_prime and n > 1:
#     print(n, 'is a prime number')
# else:
#     print(n, 'is not a prime number')



# 11 Write a program to print the sum of digits of given numbers
# number = int(input('Enter the number:'))
# sum = 0
# while number>0:
#     digit = number % 10
#     sum += digit
#     number = number - digit
#     number = int(number / 10)
# print(sum)


# 12 write a program to check whether the given number is palendrome or not
# n = int(input('Enter the number:'))
# tem = n
# rev = 0
# while n>0:
#     digit = n% 10
#     rev = rev *10 +digit
#     n = int(n/10)
# if tem == rev:
#     print('Given number is palindrome')
# else:
#     print('Not palindrome')


#13  write a python program to print the reverse of number
# n = int(input('Enter the number:'))
# rev = 0
# while n>0:
#     digit = n%10
#     rev = rev *10 +digit
#     n = int(n/10)
# print(rev)

# 14 write a python program to print the multiplication table
# n = int(input('Enter the number:'))
# i = 1
# while i<=10:
#     print(n*i)
#     i+=1


# 15 Write a python program to print the largest numbers of n numbers
# n = int(input('Enter the value of n:'))
# large = None
# i=1
# while i<=n:
#     num = int(input('Enter the number: '))
#     if large is None or num>large:
#         large = num
#     i+=1
# print('Largest number is',large)


# 16 Write a python program to print the smallest number of n numbers
# n = int(input('Enter the value of n:'))
# small = None
# i=1
# while i<=n:
#     num = int(input('Enter the number: '))
#     if small is None or num<small:
#         small = num
#     i+=1
# print('Largest number is',small)