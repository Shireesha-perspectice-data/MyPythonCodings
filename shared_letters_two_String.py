# Define a function that return commonly shared letters of two string.
def shared_letters(str1,str2):
	return len(set(str1) & set(str2))
print(shared_letters("Data Science","Python"))