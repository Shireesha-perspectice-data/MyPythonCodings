def fun(my_list):
	prime=[ ]
	for i in range(my_list):
		c=0
		print(i,(c,"c val"),"i 1st")
		print("---------")
		for j in range(1,i):
			print(j,"j 1st")
			if i%j==0: # 1)2(2 here i=2,j=1
				c+=1
				print(j,"val",i)
				print("==========")
			else:
				print("000000",i,j)
		if c==1:
			prime.append(i)
			print(i,"prime value")
	return prime,"******"
print(fun(my_list=6))
		
