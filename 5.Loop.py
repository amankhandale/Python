
# & Loop ( Loops are used to repeat instrustions).

# count = 1
# while count <=5 :    
#     print("Hello")
#     count += 1

# i = 1
# while i <=5 :
#     print("ark", i)
#     i+=1

# ! Print numbers from 1 to 5.
# i = 1
# while i <=5:
#     print(i)
#     i+=1

# ! Print number from 5 to 1 (reverse).
# i = 5
# while i >= 6:
#     print(i)
#     i-=1

# ? Print Number from 1 to 100.

# i = 1
# while i <=100:
#     print(i)
#     i+=1

# ? Print Number from 100 to 1.

# i = 100
# while i >=1:
#     print(i)
#     i-=1

# ? Print the multiplication table of a number n.

# i = 1
# n = 3
# while i <= 10:
#     print(n*i)
#     i+=1

# ? Print the element of the following list using list : [1,4,9,16,25,36,49,64,81,100]

# num = [1,4,9,16,25,36,49,64,81,100]

# idx = 0
# while idx < len(num):
#     print(num[idx])
#     idx+=1

# ? Print the element of the following list using tuple : (1,4,9,16,25,36,49,64,81,100)

# num = (1,4,9,16,25,36,49,64,81,100)

# x = 16
# i = 0

# while i < len(num):
#     if(num[i] == x):
#         print("Search Found at index", i)
#         break
#     else:
#         print("Finding...")
#     i+=1

# ! Break : Terminates the process

# i = 1
# while i <= 5:
#     print(i)
#     if (i == 4):
#         break
#     i+=1

# ! Continue : Skips the process and continues in  next iteration

# i = 0
# while i <= 5:
#     if (i == 3):
#         i+=1
#         continue # skip
#     print(i)
#     i+=1

# ! Print Even numbers using continues

# i = 1
# while i <=10:
#     if(i%2 != 0):
#         i+=1
#         continue
#     print(i)
#     i+=1

# ! FOR loop: used for sequential traversal.for traversing list, string, tuple

# str = "ArkSolitude"
# for char in str:
#     if(char == "d"):
#         print("found d")
#         break
#     print(char)
# else:
#     print("End")

# ? Print the elements of the following list using a loop:

# list = [1,4,9,16,25,36,49,64,81,100]

# for num in list:
#     print(num)

# ? Search for a number x in this tuple using loops:

# tup = (1,4,9,16,25,36,49,64,81,100)
# x = 64
# idx = 0
# for num in tup:
#     if(num == x):
#         print("Search Found at idx", idx)
#     idx+=1

# ! Range: Funtion that returns a sequence of number starting from 0 by default and incerment by 1 and stop before a specified number
# ^ range = (start?, stop, step?)

# seq = range(5)
# for i in seq:
#     print(i)

# ! Range Funtion (start , stop , step)

# for i in range(10): #range(stop)
#     print(i)

# for i in range(5,10): # range (start, stop)
#     print(i)

# for i in range(2, 10, 2): # range (start, stop , step)
#     print(i) 
 
# ? Print even numbers using range function:

# for i in range(2, 100, 2):
#     print(i)

# ? Print odd numbers using range function:

# for i in range(1 , 100, 2):
#     print(i)

# ? Print numbers from 1 to 100:

# for i in range(1, 101):
#     print(i)

# ? Print numbers from 100 to 1:

# for i in range(100, 0, -1):
#     print(i)

# ? Print the multiplication table of a number n

# n = int(input("Enter a number"))

# for i in range(1, 11):
#     print(n*i)
    
# ! Pass statement: Null statement (Skip)

# for i in range(10):
#     pass
# print("imp work")

# ? Write a program to find sum of first n numbers. (using while).
# ^ Using For
# n = 5

# sum = 0
# for i in range(1, n+1):
#     sum += i

# print("Total sum is ", sum )

# ^ Using While

# n = 7
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i+=1
# print("Total sum = ", sum)


# ? Write a program to find the factorial of first n numbers. (Using For).
# ^ Using While
# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact*=i
#     i+=1
# print("Factorial = ", fact)

# ^ Using For
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial =", fact)
