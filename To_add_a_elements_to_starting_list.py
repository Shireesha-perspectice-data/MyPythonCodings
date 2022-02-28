#To add a element to starting a list 
def fun(list_e):
    list_e.insert(0,1)
    return list_e
print(fun([2, 3, 4, 5, 6, 7, 8, 9, 1]))