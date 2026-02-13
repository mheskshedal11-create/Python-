'''
 conditonal expression= a one line shortcut for the if-else satement (ternary operator)
                        print or assign one of two values based on a conditon 
                        x if conditon else y
'''


num=2
a=3
b=6
result= 'Even' if num%2==0 else "ODD" 
print(result)

max_number= f'max number is {a}' if a>b else f'b is max number{b}'
print(max_number)