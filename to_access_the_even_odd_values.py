even=[]
odd=[]
def fun(n):
	for i in range(n):
		if i%2==0:
			even.append(i)
		else:odd.append(i)
	return even,odd;
print(fun(11))