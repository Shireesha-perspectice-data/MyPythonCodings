#Python program to swap two number without usinvariableg third 
# a = int(input("please give first number a: "))
# b = int(input("please give second number b: "))
def swap_var(a,b):
	a=a-b
	b=a+b
	a=b-a
	return ("value of a is : ", a),("value of b is : ", b)
print(swap_var(a = int(input("please give first number a: ")),
b = int(input("please give second number b: "))))