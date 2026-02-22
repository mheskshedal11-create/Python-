'''
Membership operators = used to test whether a value or variable is found in a sequence 
( stirng , list, tuple, set or dictionary )
1) in
2) not in 

'''
word = 'APPLE'
letter= input('Guess a letter in the secret word: ').upper()
if letter in word:
    print(f'there is a {letter}')
else:
    print(f'{letter } was not found')


'''
List comprehension== a concise way to create lists in python  compact and easier to read than 
traditional loops [ expression for value in iterable in condition ]
'''

doubles=[]
for x in range(1,11):
    doubles.append(x * 2)
print(doubles)


double=[x *2 for x in range(1, 11)]
print(double)

tuples= [y *3  for y in range(1,11)]

print(tuple)

fruits= ['apple','mango','banana','coconut']
fruits=[fruit.upper() for fruit in fruits]
print(fruits)


numbers=[1,-2,3,-4,5,-6]
positive_nums= [num for num in numbers if num>=0]
even_nums= [num for num in numbers if num %2==0]
print(positive_nums)
print(even_nums)

