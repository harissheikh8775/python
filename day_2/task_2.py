# type error checking

# len(123) #bad code
len("123") #good code

# type checking
print(type(123))
print(type("hello"))
print(type(True))
print(type(1.234))

# type conversion
print("123"+"456")
print(int(123)+int(456))

# we can't convert "abc" to integer abc

# ''' Make this line of code run without errors.'''
"""print("Number of letters in your name : "+ len(input("Enter your name: ")))"""

print("Number of letters in your name : "+ str(len(input("Enter your name"))))
