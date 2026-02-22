'''
variable scope== where a variable is visible and accessible
scope resolution= (LEGB) local->Enclosed->Global->built-in
'''

# def fun1():
#     x=1 #local scope
#     print(x)

# def fun2():
#     x=3  #local scope
#     print(x)

# fun1()

# fun2()



def fun1():
    x=1 # enclosed version
    def fun2():
        print(x)
    fun2()

fun1()

