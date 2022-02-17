import re
import random
#names=['Rahul','Rajesh','Manoj','Manvika']
def dictionary_form(names):
	d={}
	x=10
	count=0
	for j in range(x):
		l=random.choice(names)
		d[count]=1
		count+=1
		print(d)
dictionary_form(names=['Rahul','Rajesh','Manoj','Manvika'])