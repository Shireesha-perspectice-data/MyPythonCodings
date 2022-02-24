import re
import random
names=['Ram','Rajesh','Manoj','Arun','malvia','vinodh','Manasa']
def listing():
	list=[]
	x=100000
	for i in range(x):
		l=random.choice(names)
		list.append(l)
		#print(list)

def dict():
	d={}
	x=100000
	count=0
	for j in range(x):
		l=random.choice(names)
		d[count]=1
		count+=1
		#print(d)


import time
t1=time.time()
listing()

t2=time.time()
print(t2-t1)
t3=time.time()
dict()

t4=time.time()
print(t4-t3)
	