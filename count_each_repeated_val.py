count=0
def fun(list):
	return {each:list.count(each) for each in list}
print(fun(list=[1,2,2,2,2,3,4,4,5,6,6,7,7,7,7]))