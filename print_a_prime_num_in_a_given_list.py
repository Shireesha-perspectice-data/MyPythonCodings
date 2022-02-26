# print the prime numbers
def fun(l):
    count=1;
    for i in l:
        if i%2==1:
            #count+=1
            print(i)
    return count
print(fun([2,4,7,9,4,5,6,11]))