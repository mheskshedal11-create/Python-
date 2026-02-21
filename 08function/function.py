'''
function: a block of reusable code place ( )after the function name to invoke it.

'''
# def display_invoice(username,amount,due_date):
#     print(f'hello {username}')
#     print(f'your bill of ${amount} is due :{due_date}')

# display_invoice('mahesh','100.1','10/02')


# '''
# Return: statement used to end a function and send a result back to the caller
# '''

# def addNumber(a,b):
#     z = a+b 
#     return z
# print(addNumber(2,6))




'''
Default Arguments= a default arguments value for certain parameters default is used when that argument
is omitted make your functions more flexible reduces # of arguments 
1) positional 2)Default 3)keyword  4)arbitrary 
'''

import time

# def count(start, end):
#     for x in range(start, end + 1):
#         print(x)
#         time.sleep(1)
#     print("done")

# count(1, 15)