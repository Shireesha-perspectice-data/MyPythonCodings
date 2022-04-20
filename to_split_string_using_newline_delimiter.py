#To split strings using newline delimiter  
#Initializing the string 
init_str="this is the program "

#print the Initial string 
print("Initial string", init_str)

#splitting on newline delimiter
res_list=(init_str.rstrip().split('[], '))

#printing the result
print("Resultant prifix",str(res_list))