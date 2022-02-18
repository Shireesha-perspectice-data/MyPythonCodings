def return_unique(list):
	return [i for i in list if list.count(i)==1]
print(return_unique([1,34,5,6,3,4,2,6]))