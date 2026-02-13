x=3.8
y=4
# y=-4
z=5

#round function()
# result= round(x)

#abs()
# result= abs(y)

# power()
# result=pow(z,y)

#max ()
# result=max(x,y,z)

#min()
# result=min(x,y,z)
# print(result)

# math function 
import math

# a=3.2

# print(math.pi)

# print(math.e)

# result= math.sqrt(16)# find the Square root

# result= math.ceil(a)#Round up to nearest integer

# result= math.floor(a)#Round down to nearest integer

# print(result)




#calucate circle circumference
# radius= float(input('Enter the radius of a circle: '))
# circumference=2 * math.pi *radius
# print(f'the circumference of circle is {round(circumference,2)}')# only two decimel


# calculate area of circle 
# radius= float(input('Enter the radius of a circle: '))
# # area= math.pi * radius * radius
# area= math.pi *pow(radius ,2)
# print(f'area of circle is {round(area)}')


#hypotenuse of the triangle
length = float(input('Enter Length of Triangle: '))
breadth = float(input('Enter Breadth of Triangle: '))

c = math.sqrt(pow(length, 2) + pow(breadth, 2))

print(f"The hypotenuse of the triangle is {c}")