import re
#findall to find the pattern to end of the given string.findall function  is find the holl string
sample="the sample values are observed in data.the variable is most importance in the sample"
print(re.findall(r'importance.+',sample))  # findall function 