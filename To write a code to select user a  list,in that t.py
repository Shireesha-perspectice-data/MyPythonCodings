# To write a code to select user a  list,in that to print the even numbers and also odd
def fun(var):
    return list([i if i%2==0 else list[i] for i in var ])
print(fun([1,2,3,4,5]))
print(fun(var=[1,2,3,4,5,6,7,8,9,10,12,32,14,9,31,64]))
