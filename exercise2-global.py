# Jaylon Virgil
# CSC 419 Assignment 3: Exercise 2 (python)
# --
# uses global variable to demonstrate side effects

counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # prints 1
increment()
print(counter)  # prints 2