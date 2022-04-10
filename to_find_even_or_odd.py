def find_val(dc):
	#dc={i:"even" if i%2==0 else "odd" for i in range(10)}
	for i in range(dc):
		if i%2==0:
			print("even number",i)
		else:
			print("odd number",i)
	return "given value",dc
print(find_val(dc=11))