x=10  #globle variable
def fun(): #define a function fun()
    x=20 #local variable
    print(x) # x=20 
#print(x)
fun()
print(x)  # x=10