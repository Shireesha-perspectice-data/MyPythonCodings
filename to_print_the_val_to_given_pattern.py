# Q:To write a code like that
'''
1
12
123
1234
'''
def fun(num):
    for i in num:
        for j in range(1,i+1):
            print(j,end=" ")
        print()
    print()
fun(num=[1,2,3])
fun([1,2,3,4,5,6,7])