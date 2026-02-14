'''
While Loop: execute some code while some condition remains true
'''

# name=input("Enter Your name: ")

# while name=="":
#     print('you didnot enter your name: ')
#     name=input("Enter Your name: ")
# print(f'Hello {name}')
    

# food= input("Enter a food you like (q to quite): ").lower()

# while not food=='Q':
#     print(f'you like {food}')
#     food= input("Enter another food you like (q to quite)")
# print('bye')


# num=int(input('Enter number between 1 to 10: '))

# while num <1 or num >10:
#     print(f' {num} is not valid')
#     num=int(input('Enter number between 1 to 10: s'))

# print(f'your number is {num}')




#pythn compund interest calculator

principal = 0
rate = 0
time = 0

# while principal <= 0:
#     principal = float(input('Enter the principal amount: '))
#     if principal <= 0:
#         print('Principal cannot be less than or equal to zero')

# while rate <= 0:
#     rate = float(input('Enter the rate: '))
#     if rate <= 0:
#         print('Rate cannot be less than or equal to zero')

# while time <= 0:
#     time = int(input('Enter the time in years: '))
#     if time <= 0:
#         print('Time cannot be less than or equal to zero')

# total = principal * pow((1 + rate / 100), time)

# print(f'Balance after {time} year(s): ${total:.2f}')



while True:
    principal = float(input('Enter the principal amount: '))
    if principal < 0:
        print('Principal cannot be negative')
    else:
        break

while True:
    rate = float(input('Enter the rate: '))
    if rate < 0:
        print('Rate cannot be negative')
    else:
        break

while True:
    time = int(input('Enter the time in years: '))
    if time < 0:
        print('Time cannot be negative')
    else:
        break

total = principal * pow((1 + rate / 100), time)

print(f'Balance after {time} year(s): ${total:.2f}')
