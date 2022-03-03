import random 
def fun(l):
    n=5
    p=(random.sample(l,n))
    r=sum(p),sum(l)
    return p,r
print(fun([3,4,5,2,5,1,6,7]))