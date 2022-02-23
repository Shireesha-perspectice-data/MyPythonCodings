#Q: To write a code like that
'''
1
22
333
4444
55555
666666
'''
def fun(n):
    for i in range(n+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()
fun(6)