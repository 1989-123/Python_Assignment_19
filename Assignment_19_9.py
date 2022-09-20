"""
Write a python program to create a function to 
check whether a number falls in a given range. 
"""

def f1(r, y):
    if y in r:
        print("Yes! number is falls in given range")
    else:
        print("No! number is not falls in given range")

print()
f1(range(1, 6), 6)
print()
