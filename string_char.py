def fun(var):
	return str([[i+j for i in "Abc"]for j in "Xyz"])
print(fun([[1,2,3],[1,12,3],[2,3,5]]))