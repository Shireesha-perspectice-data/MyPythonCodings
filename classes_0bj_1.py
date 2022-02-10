class myclass_01: # creat a class 
	def  __init__(self,id_no,name): # here a creat a constructor. constructor is construct the object and to initializes the object variable 
		self.id=id_no; # instance variable
		self.name=name;
		print(" student id and name")
	def ou_college(self):
		self.names="usmania";
		return "college name"

class my_class_student(myclass_01):
	print("execute the student details")

d=my_class_student(23,"siri")  #my_class_student class object is created by a  reference variable d
print("id_no",d.id,"name",d.name) # 
print(d.ou_college())
print(d.names)
#print(d.college_name)
#rint(d.college_name)
#print(d.ou_college())
