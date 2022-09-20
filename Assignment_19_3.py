"""
Write a python program to create a function which expects 
an unknown number of arguments 
"""

def f1(*t):
    for i in t:
        print(i, end=" ")

print()
f1(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print()
