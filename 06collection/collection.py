'''
collection= single variable used to store multiple values
list=[] ordered and chnageable . Duplicates ok
set={} unordered and immutable , but add/ remove ok , no duplicates
tuple=() ordered and unchnageable. duplicates ok faster
'''

# fruit=['apple','orange','banana','coconut']

# print(dir(fruit))
# print(help(fruit))

# print(fruit)
# print(fruit[2])
# print(fruit[::2])

# ================method  in list==============
# fruit[0]='pineapple'
# fruit.append('pineapple')
# fruit.remove('apple')
# fruit.insert(0,'pineapple')
# fruit.sort()
# fruit.reverse()
# fruit.clear()
# print(fruit.index('apple'))
# print(fruit.count('banana'))
 
# print(fruit)


#============================sets==================================
# fruit={'apple','orange','banana','coconut'}

# print(dir(fruit))
# print(help(fruit))

# methods
# print(len(fruit))
# print('apple' in fruit)
# fruit.add('pineapple')
# fruit.remove('apple')
# fruit.pop()# remove random element because set item are unordered
# print(fruit)


# =============================tupple==========================

fruit=('apple','orange','banana','coconut')
# print(dir(fruit))
# print(help(fruit))

print(fruit.index('apple'))
print(fruit.count('apple'))

