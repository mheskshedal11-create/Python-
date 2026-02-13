'''
String: A string is a sequence of characters enclosed in quotes
      --In Python, strings are indexed starting from 0.
'''

name= input('Enter Your full Name: ')

#len(): count also space 
# print(len(name))

#find(): find the first character. if didn't find return -1
# result= name.find('C')
# result= name.rfind('a')# find the char for last 


#capitalize(): Converts the first character of the string to uppercase and all other characters to lowercase.
# result= name.capitalize()

#uppercase():convert into uppercase
# result= name.upper()

#lowercase(): convertion lowercase
# result= name.lower()

#isdigit():Checks if all characters in a string are digits (0–9).result(True or False)
# result= name.isdigit()

#isalpha():Checks if all characters in a string are letters (a–z, A–Z).result(True or False)
# result=name.isalpha()

#count:method in Python returns the number of times a specified substring occurs in a string.
# phone_number='1-2-345-69'
# var=phone_number.count('-')
# print(f'- is repert {var} times')
# result= name.count('a')


#rplace():method returns a new string where all occurrences of a specified substring are replaced with another substring.s
# phone_number='1-2-345-69'
# result= phone_number.replace('-',' ')
# print(result)


# for all other method 
# a='mh'
# print(dir (a))


#strip(): remove the white space 
names='  alice   '
# print(names.strip())

#split():converts string → list
result= name.split()
# print(result)

#join():
result= '-'.join(name)
print(result)

a = "ram"
b = "shaym"
c = "hari"
result = "".join([a, b, c])  # list is an iterable
print(result)


'''
validate user input 
-username is no more than 12 char
-usernam must not contain space
-username must not contain digit
'''

# username = input('Enter your username: ')

# if len(username) > 12:
#     print('You cannot set the username longer than 12 characters.')
# elif ' ' in username:
#     print('Username must not contain spaces.')
# elif any(char.isdigit() for char in username):
#     print('Username must not contain digits.')
# else:
#     print(f'Username is {username}')
