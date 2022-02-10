sam="h e y i wanto say somthing"
def fun():
	str_d=''
	for i in sam:
		if i==' ':
			str_d+=','
		else:
			str_d=str_d+i;
			#str_d+=str_d+i;
	return str_d;
print(fun())