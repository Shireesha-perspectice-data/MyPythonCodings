#list_ele=[1,2,3,4,5,6,7]
def fun(str):
    return str([[i if i%2!=0 else i/2 for i in [1,2,3,4,5,6,7] ] for j in [1,2,3,4,5,6,7]])
print(fun(str))