#l=[2,3,4,5,6,4,1,2,3,7,8,9]
def unique(l):
	uniq_val=[i for i in l  if l.count(i)<=1]  #unique values i.e not repeat values
	duplicate_val=[i for i in l if l.count(i)>1]
	return ("unique values in list:",uniq_val),("duplicated val:",duplicate_val),set(duplicate_val)
print(unique([2,3,4,5,6,4,1,2,3,7,8,9]))

