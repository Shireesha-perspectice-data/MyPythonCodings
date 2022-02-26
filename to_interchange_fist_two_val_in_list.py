l=[1,2,3,4,5]
l1=[]
def fun(l):
    l1=l[0],l[1]=l[1],l[0]
    #l2=list[l[0],l[1],l[2],l[3],l[4]]
    return l1,list(l[::1])
print(fun(l=[1,2,3,4,5]))