# Find the number of digits in a given number
def Number_length(num):
	return sum(1 for i in str(num))
print(Number_length(100123456789))
