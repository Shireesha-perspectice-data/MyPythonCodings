def fun(l):
    count=[]
    for i in l:
        if i%2==0:
            print("even",i)
        else:
            print("odd",i)
fun([3,2,5,4,6,6,1,7,8])