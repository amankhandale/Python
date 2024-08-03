
# & Dictionary (Store data in a key:value pair)

# dict = {
#     "Key": "Value",
#     "Subject" : ["python", "Java", "C"],
#     "Name": "Ark",
#     "Age": 21,
#     "Straight": True,
#     "Marks": 85.7,
# }

# null_dict = {}
# null_dict["Name"] = "ARKSOLITUDE"
# print(null_dict)

# dict["Name"] = "Aman"
# dict["Age"] = 20
# print(dict)
# print(type(dict))

# ! Nesting in Dictionary

# info = {
#     "Name": "Ark Solitude",
#     "EXP" : "257",
#     "RANK" : {
#         "COC" : "TH11",
#         "VALORANT" : "PLATINUM",
#         "MOBILE LEGEND" : "EPIC",
#     }
# }

# print(info)

# ~ Dictionary Methods

# * Dictionary Keys ( Returns all keys)
# print(info.keys)
# print(list(info.keys()))
# print(type(info.keys()))

# print(info["RANK"])  #prints specific value
# print(info["Name"])

# print(len(list(info.keys())))

# * Dictionary Values (Returns all values)

# print(info.values())
# print(list(info.values()))

# * Dictionary Items (Returms all items in a key:value pair as tuple)

# print(info.items())
# print(list(info.items())) 

# pairs = (list(info.items()))
# print(pairs[2])

# * Dictionary Get ( Returns the key according to the value)

# print(info.get("RANK"))
# print(info.get("RANK2"))  # if error occurs it will return none

# * Dictionary Update (Inserts the specified items to the dictionary)

# new_dict = {"new" : "dictionary", "City" : "Pune"}
# info.update(new_dict)

# print(info)

# & Sets (Collection of unordered items. Each element must be unique & immutable0)

# Collection = {1,2,3,4,"ARK", "SOLITUDE", "AMAN", "KHANDALE", 3,4} #Ignores duplicates

# print(Collection)

# print(type(Collection))
# print(len(Collection)) # total no. of items

# ! Empty Set
 
# collection = set()  # empty set : syntax
# print(type(collection))

# ~ Sets Methods
# ^ Note: Set is  mutable. But the elements stored in the set is immutable


# * Set add ( Add items to the sets) [list & dict cannot be added becuz they are mutable]
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add("ARK")
# collection.add([5,6,7]) #mutable value : unhashable

# print(collection)

# * Set Remove( Removes items from the set)
# collection.remove(1)
# collection.remove(2)

# print(collection)

# * Set Clear( Removes all the items from the set)
# collection.clear()

# # print(collection)

# * Set Pop (Removes random values from the set)

# collection = {"Aman", "Khandale", 1,2,3,4, "Ark", "Solitude", "Python", "Coding"}

# print(collection.pop())
# print(collection.pop())

# * Set Union( Combines both sets of values & returns new)
# set1 = {1,2,3}
# set2 = {2,3,4}

# print(set1.union(set2))

# * Set Intersection( Combines common values & returns new)
# set1 = {1,2,3}
# set2 = {2,3,4}

# print(set1.intersection(set2))

# ? Store a meaning in python using dictionary

# dictionary = {
#     "table" : ("a piece of furniture", "list of fact & figures"), 
#     "cat" : "a small animal"
# }
# print(dictionary)
# print(type(dictionary))

# ? You are given a list of subjects for students.
# ? Assume one classroom is required for 1 subject.
# ? How many classroom are needed by all students

# subject = {"python", "java", "c++", "python", "javascript",
#            "java", "python", "java", "c++","c"}
# # sub1 = {"python", "java", "c++", "python", "javascript"}
# # sub2 = {"java", "python", "java", "c++","c"}

# # print(len(sub1.union(sub2)))
# print(len(subject))

# ? Write a program to enter marks of 3 subjects from the user and store them in a dictionary.
# ? Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

# Marks = {}

# eng = int (input("Enter English Marks: "))
# math = int(input("Enter Maths Marks: "))
# phy = int(input("Enter Physics Marks: "))

# Marks.update({"English" : eng,
#               "Maths" : math,
#               "Physics" : phy})

# print(Marks)

# ? Figure out a way to store 9 & 9.0 as separate values in a set
#Method 1
Set = {"9", 9.0}
print(Set)

#Method 2
values = {("Integer", 9)
          ("float", 9.0)}
print(values)