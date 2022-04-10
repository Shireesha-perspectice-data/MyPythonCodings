def dic_form(d):
	#d={i:len(i) for i in d}
	for i in d:
		if i:
			print(i,":",len(i))
	return d
print(dic_form(d=["DataScience","Python","Java","c++"]))