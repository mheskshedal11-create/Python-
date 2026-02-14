'''
nested loop: A loop within another loop (outer, inner)
outer loop:
    inner Loop:
'''

# for x in range(1,11):
#     print(x , end='-')
    
# for x in range(3):
#     for y in range(1,11):
#         print(y , end='')
#     print()


rows= int(input ("Enter the # of rows: "))
cols= int(input ("Enter the # of cols: "))
symbol= input('Enter a symbol to use: ')

for x in range(rows):
    for y in range(cols):
        print(symbol, end='')
    print()