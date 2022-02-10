class z:
	def tax(self):
		#self.taxes=234;   # instance  variable 
		self.income_tax();   # here calling instance method 
		print("the govt taxes are collected")

	def income_tax(self):
		try:
			#print (10/0)
			self.income_services();    # the reason 
			#print(10/0)
			#print("the zerodivisorError")

		except :
			print (10/2)
			#print (10/2)
			print ("the divide the number")

		#except zerodivisorError as e:
		#	print (20/4)
		#	print (" the zerodivisorError ")




	def income_services(self):
		print (22/0)
		print ("the error is raise")



a=z()
a.tax()
 

def taxes(self):
	self.tata=45;

q=taxes()
print(q.taxes())
print(q.tata)


