# string="The man who is pure, and who dares, does great things."
def fun(string):
	str_d=''
	for i in string:
		if i==' ':
			str_d+=' @*@ '
		else:
			str_d=str_d+i;
			#str_d+=str_d+i;
	return str_d;
print(fun(string="The man who is pure, and who dares, does great things."))
