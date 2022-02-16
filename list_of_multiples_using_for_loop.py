# List of multiples of first elements with second element consecutive times.
def list_of_multiples(num,length):
	lst=[]
	for i in range(length):
		lst.append(num+i*num)
	return lst
print(list_of_multiples(6,5))
