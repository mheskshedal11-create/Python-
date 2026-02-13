'''
 if= do some code only if some conditon is true 
 else do somethin elase 
'''

age=int(input('Enter You age :'))

# if age >=18:
#     print('You can drive ')
# else:
#     print('you cannot drive ')

if age < 0:
    print("You cannot set the age as negative")
elif age == 0:
    print("You cannot set the age as 0")
elif age >= 18:
    print("You can drive")
else:
    print("You cannot drive")


#boolean

is_sale = False 

if is_sale:
    print('This item is for sale')
else:
    print('This is not for sale')
