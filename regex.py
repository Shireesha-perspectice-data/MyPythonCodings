#Regular expressions

import re     #module name is  re i.e regular expression

#print(re.groupby())
#search  to find the pattern at the beginning of the given string or find the very accurence of a given string 
para="the aim all develop of the Telangana is sincerely implement all developmental schemess"
print(re.search(pattern='all develop.', string=para))  
'''
# by using search function to find the first accurrence of pattern from the string para 
#using search() to find somthing or pattern from para string
#====> search function is used to find the very first accurrence of the given string  
'''


#findall to find the pattern to end of the given string.findall function  is find the holl string
text="to explain the regular expression"
print(re.findall(r'regular.+',text))  # findall function to find the pattren from the given string


template ="it's  the basic terminology of the indeJKLPendention python "
rs=re.findall(r'of',template)  #here r is the pattern
rsr=re.findall(r'i[a-z].',template)  #findall function is used to find the pattern from the given string
print(rs)
print(rsr)
print(re.findall(r'i[a-z].+',template))    # set of charactor e.g [a-z] will match all letters from a to z
print(re.findall(r'i[a-z].*',template))   # to match all letters from a to z
print(re.findall('i[a-z][A-Z].',template))   # To find the pattern by using of findall func to match  all letters from a to z,and A to Z
print(re.findall('python',template))
print(re.findall('n^',template))


to_pairs="Manoj age is 68 Arun age is 87 Tharun age is 100 Kamal age is 98 Srija age is 95"
print(re.findall(r'[A-Z][a-z].*',to_pairs))  #here to the statement is satisfy the until the given string is satisfy
print(re.findall('[a-z]',to_pairs))    #; findall func to find the pattern from the given string
print(re.findall('[A-Z][a-z]+',to_pairs))  #findall func is used to find the pattern from the given string
'''
d={}
count=0;
for each in to_pairs:
	d[each]=d[to_pairs]+[each]
	x=y+1;
	y=x+1;
print("to print the some values")
print(each)'''

'''
\d :=  A digit
\D :=  Any charactor but not a digit (opposite to digit)
\s :=  Any Whitespace charactor
\S :=  Any charactor but not a Whitespace 
\w :=  Any Word charactor 
\W :=  Any charactor but not a word char 

'''

names="the Student Name is the Manoy "
names=re.findall(r'[A-Z][a-z]+',to_pairs)
print(names)

age=re.findall(r'\d+',to_pairs)   #\d is a digit
#print(len(age))
print(age)

d={}
x=0;
for each in names:
 	d[each]= age[x];
 	x=x+1
print(d)


