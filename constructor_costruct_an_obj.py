'''
the constructor is a special type of object/function,constructor is the construct object.i.e is an instantiating an object.
__init__method is invoke when an object is created from the class and its allows the class to initialize the instance variable/member of a class ")
'''
x=23789;  #globle variable
class car: #here creat a car class. here car is a current object
    x=20; # static variable means inside a class we are consider the static variable
    def __init__(self):
        self.x1=66;
        self.x2=345;
        print("the constructor is a special type of object/function,constructor is the construct object.i.e instantiating an object.__init__method is invoke when an object is created from the class and its allows the class to initialize the instance variable/member of a class ")
    x=56;
    print(x)
#print(x)
z=car()  #inistantiating or created an object by reference variable z
print(z.x1)  #to print instance variable x1 by using of object. instances mean related object values
print(x)
    