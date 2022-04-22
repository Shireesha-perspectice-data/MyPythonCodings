class class_name:  # to create a class name is class_name
	def class1(self):  # inside the class we are create a method, to access through the current object
		self.x1=23;  #instance variable
class class_roll_no(class_name):
	def class2(self):
		self.x2=34;
ref_obj=class_name()   #created the reference variable
print(ref_obj.class1())
print(ref_obj.x1) #to access the current variable through the object
