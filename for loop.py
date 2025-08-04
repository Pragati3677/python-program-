# 1 Write a python program to print the natural numbers
# n = int(input('Enter the value of n: '))
# for i in range(1, n + 1):
#     print(i)


# 2 Write a python program to print even numbers up to n
# n = int(input('Enter the value of n: '))
# for i in range(2, n + 1, 2):
#     print(i)


# 3 Write a python program to print odd numbers up to n
# n = int(input('Enter the value of n: '))
# for i in range(1, n + 1, 2):
#     print(i)

# 4 Write a progrma to print the square of numbers
# n = int(input('Enter the value of n: '))
# for i in range(1, n + 1): 
#     print(i * i)
 
#  5 write a program to print the sum of given sequence
# 1+1/1!+1/2!+1/3!+1/4!+1/5!+...+1/n!
# n = int(input('Enter the value of n: '))
# sum = 1
# fact = 1
# i = 1
# for i in range(1, n + 1):
#     fact *= i
#     sum += 1 / fact
#     i +=1
# print(sum)

# 6 write the program to compute the cosine series
# cos(x) = 1-x^2/2!+x^4/4!-x^6/6!+...+(-1)^n*x^(2n)/(2n)!

#7 Write a python program to check whether the square root of number is prime or not

# n = int(input('Enter the value of n: '))
# import math
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True
# sqrt_n = int(math.sqrt(n))
# if is_prime(sqrt_n):
#     print(f"The square root of {n} is {sqrt_n}, which is a prime number.")
# else:
#     print(f"The square root of {n} is {sqrt_n}, which is not a prime number.")

# 8 Write a pattern
# A B C 
# A B C
# A B C

# for i in range(3):
#     for j in range(3):
#         print(chr(65+j), end=' ')
#     print()

# 9 pattern
# A
# A B
# A B C 
# A B C D
# A B C D E

# for i in range(5):
#     for j in range(i + 1):
#         print(chr(65 + j), end=' ')
#     print()


# 10 pattern
# A B C D E
# A B C D
# A B C
# A B
# A

# for i in range(5, 0, -1):
#     for j in range(i):
#         print(chr(65 + j), end=' ')
#     print()


# 11 pattern
# 1
# 1 2 
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()


#  12 pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for i in range(1, 6):
#     for j in range(i):
#         print(i, end=' ')
#     print()