import re
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
