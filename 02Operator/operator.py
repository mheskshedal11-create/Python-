'''
Operator:An operator in Python is a symbol that performs a specific 
operation on one or more values (called operands) and returns a result.
'''

#Arithmetic Operators:Used to perform mathematical operations like addition, subtraction, multiplication, etc.
x = 10
y = 3
print(x + y)  # 13
print(x - y)  # 7
print(x * y)  # 30
print(x / y)  # 3.3333
print(x % y)  # 1
print(x ** y) # 1000
print(x // y) # 3

#Comparison Operators:Used to compare two values and return True or False.
a = 5
b = 10

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= 5)  # True
print(b <= 10) # True

#Logical Operators:Used to combine conditional statements.
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False

#Assignment Operators:assign values to variables, sometimes with an operation.
x = 5
x += 3  # x = 8
x *= 2  # x = 16
print(x)

#Identity Operators:Used to check if two variables point to the same object.
a = [1, 2]
b = a
c = [1, 2]

#  is : ture if same object
# is not : True if not the same object 
print(a is b)      # True
print(a is c)      # False
print(a is not c)  # True


# Membership Operators:Used to check if a value exists in a sequence (like a list, string, or tuple).


fruits = ["apple", "banana", "mango"]
#in :ture if value exists
# not in : ture if value does not exits
print("apple" in fruits)      # True
print("grape" in fruits)      # False
print("grape" not in fruits)  # True

# example  
username = input("Enter username: ")

allowed_users = ["raj", "maya", "hero"]

if username in allowed_users:
    print("Welcome!")
else:
    print("Access denied")

