def fun(lst,lsts,ex_lst):
    lst.insert(2,245) # add an element instead of a index of 2
    print(len(lst))
    lst.pop(0)  # pop the zero element in a list  
    #print(lst)
    lsts.insert(0,435600) 
    ex_lst.extend(lsts)  #To append elements from another list to the current list, use the extend() method.
    return lst,lsts,ex_lst
#print(len(lst))
print(fun([5,6,7],[1,23,3],[1,0,4,5,333]))
