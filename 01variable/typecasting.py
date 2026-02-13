'''
Type Casting: The process of converting a value of one data type to another (string , integer, float and boolena )
There are two types of TypeCasting:
1) Explicit 
2) Implicit
'''

# Implicit :Implicit means Python automatically decides or converts data types
#  when needed, without the programmer explicitly telling it to do so.
name='Hero'
age=21 
gpa=1.9
student=True
y= age/gpa
print(y)
print(type(y)) #float 
# print(type(name))#str
# print(type(age))#int
# print(type(gpa))#float
# print(type(student))#bool

#explicit: Explicit means clearly defined and directly written by the programmer 

age=float(age)
print(type(age))# float 

gpa= int(gpa)
print(type(gpa))#int

student=str(student)
print(student)
print(type(student))