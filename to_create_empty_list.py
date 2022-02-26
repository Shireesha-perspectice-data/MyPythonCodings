def fun(l):
    if l:
        print("list of elements",l)
        l.clear()
        print("Now list becomes empty",l)
    else:
        print("list is already empty",l)
fun([2,3,4,5])