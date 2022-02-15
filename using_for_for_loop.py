sample=[1,23,24,25,26,27]# here we use for loop,here we write code high,but list comprehension we use single code line
s=[]
for i in sample:
    i=i**3
    s.append(i)
print(s)
print(i)