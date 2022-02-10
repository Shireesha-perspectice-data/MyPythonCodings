#set consider a unique values.it doesn't consider the duplicated values.
my_set={'sir','rams','dataScience','data','sql'}
my_list={'rani','dataScience','dm','sir'}

print(my_set.union(my_list)) #here toconsider the both values not repeate the values,only unic values to consider both 
print(my_list.intersection(my_set)) #here in two set we are taking only equal values 
print(my_list.union(my_set))
print(my_list&my_set) # '&'' it also like as the intersection 
print(my_list | my_set) # '|' it also like as union 