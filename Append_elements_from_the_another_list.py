# To append elements from the another list to the current list,use the extend()method.
def fun(list_ele,list_val):
    list_ele.extend(list_val)
    return list_ele
fun([3,4,5,6,0,1,2,3,66666],[7,8,9,10,11,15])