import re
import random
#names=['Rahul','Rajesh','Manoj','Manvika']
def listing(names):
	list=[]
	x=100000
	for i in range(x):
		l=random.choice(names)
		list.append(l)
		print(list)
		break;
print(listing(names=['Rahul','Rajesh','Manoj','Manvika']))