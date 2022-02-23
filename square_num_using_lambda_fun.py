#Q: write a code of square of numbers using lambda function.
def fun(val):
    item = map(lambda x:x**2 ,val)
    for i in item:
        print(i)
fun(val=[1,2,3,4,5])
fun([5,6,7,8,9,10])