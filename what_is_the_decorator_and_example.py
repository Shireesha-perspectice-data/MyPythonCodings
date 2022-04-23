#Decorator:
#    Decorator is just a function that takes another function as an arguement, add some kind of functionality and then return another function 
def decorator_fun(func):
	def inner_fun():
		print("inner_fun worked")
		return func()
	print("decorator_fun working")
	return inner_fun

def show():
	print("it working")
decorator_show=decorator_fun(show)
decorator_show()