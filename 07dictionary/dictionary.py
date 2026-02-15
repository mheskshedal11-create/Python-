'''
Dictionary= a collection of {key:value } paris orderd and changeable. no dulicates

'''

capitals={
    'Nepal':"Kathmandu",
    'China':'Beging',
    "South_Korea":'Seoul',
    'japan':'tokyo'
}

# print(dir(capitals))
# print(help(capitals))

#check the vaule we use get method
# print(capitals.get('Nepal'))

#add and update key and vaule
# capitals.update({'China':'Sanghai'})#update
# capitals.update({'Gernamy':'Berlin'})#add new 

#remvove (key and value)
# capitals.pop()# remove key and value from the last
# capitals.pop('South_Korea')#remove specific


#for clear the dictionary
# capitals.clear()#clear hole dictionary



#get all keys from dictionary and provide in list 
# keys=capitals.keys()
# for key in keys:
#     print(key)
# print(keys)


#for values 
# values= capitals.values()
# for value in values:
#     print(value)
# print(values)


#items: The items() method returns all key–value pairs in the dictionary as 
# a special object called a dict_items object (which behaves like a list of tuples).

# item = capitals.items()
# for key,value in item:
#     print(f'{key}:{value}')
# print(item)
 


 #concession stand program

menu={
    'pizza':30,
    'nachos':40,
    'popcorn':50,
    'fries':60,
    'chips':70,
    'soda':30
}
cart=[]
total=0


print('----------menu-----------------')
for key, value in menu.items():
    print(f'{key:10}: NR {value}')

print('-----------------------------------')
while True:
    food=input('Select an item (q to quite): ').lower()
    if food=='q':
        break
    elif menu.get(food) is not None:
        cart.append(food)


print('-----------your cart----------------')
for food in cart:
    total= total + menu.get(food)
    print(food , end=' ')

print()
print(f'total is {total} ')