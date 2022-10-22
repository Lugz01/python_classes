#Data types

"""
Data types
"""

#Working number data types
#Integers, Floats and complexes

print("Integer:", 100)

#Checking for  a data type
print(type("Said"))

# print(bool())
print(int(10.7), type(int(10.7)))

# print()
# Opeartors
print(12%5)

# import time

# while True:
#     print("Tim")
    # time.sleep((2))

#Variables in programming

# variable_name = value_
# name = "Said"

# print("Said")

#convention for naming variables
firstname =  "Said"

#pascasl naming convention
first_name = "Mohammed"

#camel naming convention
firstName = "Emmanuel"

#using keywords
# [True, False, type, and, or, print, input, if, for]

print(firstname)
print(first_name)
print(firstName)


#string Concatenation
first_name = "Saheed"
second_name = "Mohd"

names = first_name + second_name

#multiplication sign on strings
# print(names*100)

name = "tiMoothy"

print(name.capitalize())

print(name.lower())

print(name.upper())

print(name.count("o"))

print(name.endswith("thy"))

print(name.startswith("tiM"))

print(name.find("y"))

# person:str = "Saheed"

age:str = 'dfghjk'

print(age.capitalize())


#Data structures
#list []

names_of_people:list = ["Saheed", "Tim", "prince", "mohammed"]

print(names_of_people)

names_of_people.append("Ibrahim")
print(names_of_people)

names_of_people.insert(0, "Sani")
print(names_of_people)

other_names =["Samuel", "James"]
names_of_people.extend(other_names)
print(names_of_people)

names_of_people.sort()
print(names_of_people)

names_of_people.reverse()
print(names_of_people)

names_of_people.pop()
print(names_of_people)

names_of_people.remove('Tim')
print(names_of_people)


if "faruk" not in names_of_people:
    names_of_people.append("faruk")
    print((names_of_people))

print(len(names_of_people))   


#listing slicing
# print(names_of_people[0:5])
# print(names_of_people[0])


# for names in range(len(names_of_people)):
#     print(names, names_of_people[names])

for num in range(5):
    if num is 5:
        break
    print(num)

# names_of_people.clear()
# print((names_of_people))

