num=int(input("enter the value n:"))
a=0
b=1
#sum=0 # here where we start  series 0.
count=0   # 
while a<=num:
    print(count)
    count+=1
    a=b
    b=count
    count=a+b