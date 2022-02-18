def last_digit(a,b,c):
	return str(a*b)[-1]==str(c)[-1]
print(last_digit(12,2,4))  #12*2=24,4
print(last_digit(23,4,5))    # 3*4=12;2!=5