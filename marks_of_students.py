# x=int(input("enter the first subject integer"))
# y=int(input("enter the second subject integer"))
# z=int(input("enter the third subject integer"))
def func(x,y,z):
	sum=(x+y+z)
	if sum<270 and sum>240:
		print("suma recieved A+")
	elif sum<210 and sum >180:
		print("rama recieved A Grade")
	elif sum <130 and sum >100:
		print("raju recieved B Grade")
	else:
		print("remains are not recieved certificates")
func(220,26,13)
func(234,456,56)
