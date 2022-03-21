def fun(list):
	word=" "
	double=list
	for i in range(len(list)):
		word=list[2*i]
		double.insert(2*i+1,word)
	return double
print(fun([1,"Richard Koch",2,"Devid Allen"]))
