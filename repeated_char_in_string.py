def fun(string):
	return str(set(string)),{each:string.count(each) for each in string }
print(fun(string="DataScience"))