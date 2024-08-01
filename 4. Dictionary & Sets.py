
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

info = {
    "Name": "Ark Solitude",
    "EXP" : "257",
    "RANK" : {
        "COC" : "TH11",
        "VALORANT" : "PLATINUM",
        "MOBILE LEGEND" : "EPIC",
    }
}

# print(info)

# ~ Dictionary Methods

# ! Dictionary Keys ( Returns all keys)
# print(info.keys)
# print(list(info.keys()))
# print(type(info.keys()))

# print(info["RANK"])  #prints specific value
# print(info["Name"])

# print(len(list(info.keys())))

# ! Dictionary Values (Returns all values)

# print(info.values())
# print(list(info.values()))

# ! Dictionary Items (Returms all items in a key:value pair as tuple)

# print(info.items())
# print(list(info.items())) 

# pairs = (list(info.items()))
# print(pairs[2])

# ! Dictionary Get ( Returns the key according to the value)

# print(info.get("RANK"))
# print(info.get("RANK2"))  # if error occurs it will return none

# ! Dictionary Update (Inserts the specified items to the dictionary)

new_dict = {"new" : "dictionary", "City" : "Pune"}
info.update(new_dict)

print(info)