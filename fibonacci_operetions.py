def fib(x):
    a,b=0,1
    c=0
    while a<=x:
        print(a,end=',')
        c+=1
        print(c)
        a,b=b,a+b

fib(x=int(input("x:")))
#0,1,1,2,3,5

l1={1,1.2,(2,3,4),23,4,'sir'}
print(l1)