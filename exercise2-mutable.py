# Jaylon Virgil
# CSC 419 Assignment 3: Exercise 2 (python)
# --
# uses mutable data types as default parameters
# to demonstrate side effects

def addToList(item, lst=[]):
    lst.append(item)
    return lst

print(addToList(1))  # prints [1]
print(addToList(2))  # prints [1, 2]
print(addToList(3))  # prints [1, 2, 3]