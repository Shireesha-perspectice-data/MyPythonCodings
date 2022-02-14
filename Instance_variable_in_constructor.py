class car:
    x=34;
    def __init__(self,dat):  #here creat a constructor with self keyword and parameter 
        self.datas="the function";  #instance variable
        self.data="the method"        # initialization means to assigning a some value
        print("hii")  # to print string statement
an_instance=car("Constructor")  # instantiating or creat an object by reference variable an_instance
print(an_instance.datas)  #to print a instance variable/ instances "datas" by through the  car object 