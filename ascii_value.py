# ch=input("enter a char")
# print(ord(ch))

def fib(x):
	a,b=0,1
	while a<=x:
		print(a,' ')
		a,b=b,a+b;

print(fib(12))