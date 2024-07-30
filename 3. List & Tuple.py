
# ! Lists (Creates Mutable sequence of value)
# marks1 = 94.40
# marks2 = 85.53
# marks3 = 74.76
# marks4 = 46.23

# marks = [94.4, 85.53, 74.76]
# print (marks)
# print(type(marks))
# print(marks[1])
# print(len(marks))

# ! Its mutable cuz any type of class can be stored in a list
# student = ["Ark", 21 , "Pune"]
# print(student)

#! Slicing in List
# marks = [85, 74, 23, 90, 30]
# print(marks[1:3])
# print(marks[-4:-1])

# ~ List Methods
# ^ List Append (Adds one element at the end)
# list = [2, 1, 3]
# list.append(4)
# print(list)

# ^ List Sort (Sorts in ascending order) [Reverse = Desending order]
# list.sort(reverse=True)
# print(list)

# ^ List Reverse (Reverses the list)
# list = ['a', 'b', 'c', 'd']
# list.reverse()
# print(list)

# ^ List Insert (Insert element at index) {list.insert(index , element)}
# list = [2, 1, 3, 4]
# list.insert(1, 6)
# print(list)

# ^ List Remove (Removes first occurence of element)
# list = [2, 1, 3, 1]
# list.remove(1)
# print(list)

# ^ List Pop (Removes element at index)
# list = [2, 1, 3, 1]
# list.pop(2)
# print(list)

# ! Tuples (Creates Immmutable sequences of values)

# tuple = (1, 2 ,3 ,4)
# print(tuple[0])

# tup = ()
# print(type(tup))

# ? Write a program to ask user to enter name of their 3 fav movies & store them in a list

# movies = []
# mov1 = input("Enter 1st movie")
# mov2 = input("Enter 2nd movie")
# mov3 = input("Enter 3rd movie")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

# ? Write a program to check if a list contains a palindrome of elements

# list1 = [1,2,3,2,1]
# list2 = [1,2,3]

# copy_list1 = list1.copy()
# copy_list1.reverse()
# copy_list2 = list2.copy()
# copy_list2.reverse()

# if(copy_list1 == list1):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# if(copy_list2 == list2):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# ? Write a program to count the number of students with the "A" grade in the following tuple

# grade = ("C", "D", "A", "B", "B", "A")
# print(grade.count("C"))

# ? Store the above value in a list & store them from "A" to "D".

# list = ["B", "C", "A", "D"]
# list.sort()
# print(list)