# List operations
#####list.append(),pop(),insert() takes exactly one argument
#list=[(3,2.5,5,6,"hey",7,6,"hi"),1,2,3,4,5,8,45]
def fun(list):
    list.pop(0) #index of zero (3,2.5,5,6,'hey',7,6,'hi') is pop    
    list.append("Rabbit")  # to add an element at the end of the list
    list.insert(2,"Animals") # insert the 'Animals' instead of 2
    list[3]={"List","Elements"}
    list[3:5]=["items","variables"]
    return list

print(fun(list=[(3,2.5,5,6,"hey",7,6,"hi"),1,2,3,4,5,])) 