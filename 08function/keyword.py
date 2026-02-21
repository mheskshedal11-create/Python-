'''
keyword arguments= an argument preceded by an identifier helps with readability
order of arguments doesn't matter
1)positional 2) default 3) keyword 4) arbitrary
'''


def hello(greeting, title, first, last):
    print(f'{greeting} {title} {first} {last}')

hello('hello','MR','dip','mr.')



#arbitary arguments
'''
 *args =allows you to pass multiple non-key arguments( tuple)
 **kwargs =allows you to pass multiple keyword argments(dictionary)
* unpacking operator
'''

# def add(*nums):
#     total=0
#     for num in nums:
#         total += num
#     return total

# print(add(1,2,3))


# def dispaly_name(*args):
#     for arg in args:
#         print(arg,end=' ')
# dispaly_name('bro','','code')


# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key} : {value}')

# print_address(street='123', city='dhagadhi', state=3200, zip=1526)


def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg ,end = ' ')
    print()

    if 'apt' in kwargs:
        print (f'{kwargs.get('street')},{kwargs.get('apt')}')
    else:
        print (f'{kwargs.get('street')}')
        print(f'{kwargs.get('city')}{kwargs.get('state')},{kwargs.get('zip')}')

shipping_label('Dr.','Spongebob','Squarepants','III',
               apt='kerodsds',
                street='123',
                city='dhagadhi',
                state=3200, 
                zip=1526

               )
