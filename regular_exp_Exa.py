import re
names="the Student Name is the Manoy and his age is 54.the Student Name of Madhu and his age is 45 "
namess=re.findall(r'[A-Z][a-z]+',names)
print(namess)

age=re.findall(r'\d+',names)   #\d is a digit
print(len(age))
print(age)

d={}
x=0;
for each in (age):
 	d[each]= age[x];

 	x=x+1
print(d)


