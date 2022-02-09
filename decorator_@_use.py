def smart_phone(fun_name):
	def inner(x,y):
	
		if y==0:
			print("the value is execute")
		else:
			print("the value is not accurence")
			return fun_name(x,y)
	return inner;
print("hii")
#@smart_phone  # here to modifiy the behaviour of the anether function 
def divide(a,b):
	return a/b;
divide=smart_phone(divide)
print(divide(1,2))


