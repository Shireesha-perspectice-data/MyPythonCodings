import re
to_pairs="Manoj age is 68 Arun age is 87 Tharun age is 100 Kamal age is 98 Srija age is 95"
print(re.findall(r'[A-Z][a-z].*',to_pairs))  #37 line
# print(re.findall('[a-z]',to_pairs))    #38 line; findall func to find the pattern from the given string
# print(re.findall('[A-Z][a-z]+',to_pairs))  #findall func is used to find the pattern from the given string
d={}
count=0;
for each in to_pairs:
  	d[each]=d[to_pairs]+[each]
  	x=y+1;
  	y=x+1;
print("to print the some values")
print(each)

'''
\d :=  A digit
\D :=  Any charactor but not a digit (opposite to digit)
\s :=  Any Whitespace charactor
\S :=  Any charactor but not a Whitespace 
\w :=  Any Word charactor 
\W :=  Any charactor but not a word char 

'''
