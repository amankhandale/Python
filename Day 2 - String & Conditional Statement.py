
# ! Basic String function 
# str1 = "This is a string.\nwe are creating it in python"
# str2 = "This is the second line"
# print(str1)

# ! Concatenation (Combines multiple string functions )
# str3 = "Ark"
# str4 = "Solitude"
# final_str = str3+str4
# print(final_str)

# ! Length (Length of character)
# str5 = "Aman"
# str6 = "Khandale"
# len1 = len(str5)
# print(len1)
# len2 = len(str6)
# print(len2)
# final_string = str5+str6
# len3 = len
# print(final_string)
# print(len(final_string))

# ! Indexing (Access String's Character)
# ^Note: You can only acccess character, malipulating the character is denied
# str = "Aman"
# ch = str[3]
# print(ch)

# ! Slicing (Accessing bunch of characters of string)
# str = "Aman Khandale"
# print(str[5:9])
# print(str[:5])

# ! Negative Indexing( Accessing characters backward)
# str = "Apple"
# print(str[-5:-2])

# ~ Additional String Functions 
# ^ Ends with (Returns True if the string ends with the substr)
# str = "this is a string function"
# str = str.endswith("ion")
# print(str)

# ^ Capitalize (Makes the first character capital)
# str = "this is a string function"
# str = str.capitalize()
# print(str)

# ^ Replace (Replaces all the occurences of old )
# str = "this is a string function"
# print(str.replace("string","replace"))

# ^ Find (Returns 1st index of the 1st occurer)
# str = "this is a string function"
# print(str.find("g"))

# ^ Count (Counts the occurence of substr)
# str = "this is a string function"
# print(str.count("s"))

#?  Write a program to input user's first name & print its length
#? Write a program to count the occurence of certain character in string
# str = input("Enter your name: ")
# print("your name is ",str)
# print(str.count("a"))        #Count specific character
# len = len(str)              #Length of string
# print(len)

# ! Conditional Statements
# ^ IF statement
# age = 16

# if(age >= 18): # if the age is greater than 18 then print the below statement
#     print("Eligible for voting and applying for license")

# ^ ELIF statement
# light = "pink"

# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("GO")
# elif(light == "yellow"):
#     print("wait")
# else:
#     print("Light is Broken")

# print("end of code")

# ^ ELSE statement
# age = 16

# if(age >= 18):
#     print("can vote")
# else:
#     print("Not Eligible")

# ~ Grade student based on marks using conditional statement
# marks = int(input("enter student marks: "))

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#    grade = "B"
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# elif(marks >= 60 and marks < 70):
#     grade = "D"
# else:
#     grade = "Fail"

# print("grade of the student ->", grade)

# ! Nesting (conditional statement inside a another conditional statement)
# age = 96

# if(age >= 18):
#     if(age >=80):
#         print("too old to drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")

# ? Write a program to check if a number entered by the user is odd or even.
# num = int(input("Enter a number: "))

# rem = num % 2

# if(rem == 0):
#     print("even")
# else:
#     print("odd")

# ? Write a program to find the greatest of 4 numbers entered by the user.
# a = int(input("Enter First number: "))
# b = int(input("Enter Second number: "))
# c = int(input("Enter Third number: "))
# d = int(input("Enter Forth number: "))

# if(a > b and a > c and a > d):
#     print("first number is largest:",a)
# elif(b > a and b > c and b > d):
#     print("second number is largest:",b)
# elif(c > a and c > b and c > d):
#     print("third number is largest:",c)
# else:
#     print("forth number is largest",d)

# ? Write a program to check if a number is a multiple of 7 or not
num = int(input("Enter a number: "))

if(num % 4 == 0):
    print("multiple of 4")
else:
    print("not a multiple")