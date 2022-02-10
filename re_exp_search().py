import re     #module name is  re i.e regular expression

#print(re.groupby())
#search  to find the pattern at the beginning of the given string or find the very accurence of a given string 
para="the aim all develop of the Telangana is sincerely implement all developmental schemess"
print(re.search(pattern='all develop.', string=para))  

#====> search function is used to find the very first accurrence of the given string  
