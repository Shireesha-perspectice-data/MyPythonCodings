#write a Python program to print prime Numbers  Between 1 to 100
for num in range(1,100):
    if all(num%i!=0 for i in range(2,num)):
        print(num)
