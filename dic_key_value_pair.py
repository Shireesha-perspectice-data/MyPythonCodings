def fun(words,values):
	dic_a={i:j for i,j in zip(words,values) }
	return dic_a
print(fun(words=["Name","Age","Gender","month","Salary"],values=["Ram",22,"Male",8,650000]))