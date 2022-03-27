# Adding Two Numbers using Lambda Function 
def add_n(n):
	return lambda x:x+n
adds_n=lambda n:lambda x:x+n
added_n=adds_n(10)
print(added_n(3))
