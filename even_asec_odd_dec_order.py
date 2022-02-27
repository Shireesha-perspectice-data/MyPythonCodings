even=[]
odd=[]
#n=[1,2,3,4,5,6]
def fun(n):
    for i in n:
        #print(i)
        if i%2==0:
            even.append(i)
            even.sort()
            print(even)
             
        else:
            #print("odd values",i)
            odd.append(i)
            odd.sort()
            print(odd)
    return ["list of values:",n],even,odd[::-1],
print(fun(n=[10,1,2,9,3,4,5,6]))
