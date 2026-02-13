#python weight converter

weight = float(input('Enter your weight: '))
unit = input('Choose unit (Kilogram for K and Pounds for P): ').upper()

if unit == 'K':
    converted = weight * 2.205
    print(f"{weight} Kilograms = {converted:.2f} Pounds")
elif unit == 'P':
    converted = weight / 2.205
    print(f"{weight} Pounds = {converted:.2f} Kilograms")
else:
    print('Invalid unit')
