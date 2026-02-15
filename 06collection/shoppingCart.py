foods=[]
prices=[]
total=0

while True:
    food= input('Enter a food to buy (q to quit): ').lower()
    if food=='q':
        break
    else: 
        price=int(input(f'Enter the  price of a {food}:rs '))
        foods.append(food)
        prices.append(price)

print('-----your cart-----')

for food in foods:
    print(food , end = ' ')

for price in prices:
    total= total+ price

print()
print(f"you total is: rs {total}")