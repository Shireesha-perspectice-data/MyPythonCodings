dic={}
def fun(dic):
	# dic={"Name":"Harish","ID.No":103452,"salary":750000,"married":True}
	return dic.keys(),dic.values(),[dic["Name"],dic['salary']]
print(fun(dic={"Name":"Harish","ID.No":103452,"salary":750000,"married":True}))