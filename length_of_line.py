def line_length(val1,val2):
	[x1,y1],[x2,y2]=val1,val2;
	return round(((x1-x2)**2 + (y1-y2)**2)**0.10,5) #The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
print(line_length([1,2],[2,3]))

'''
round(number,digits) # round() function syntax
number: Required.The number to be rounded
digits: Optional.The number of decimals to use when rounding the number. Default is 0
'''