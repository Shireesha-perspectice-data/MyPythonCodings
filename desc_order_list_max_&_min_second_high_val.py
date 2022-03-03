def fun(l):
    r=l.sort()
    return l[::-1],("second highest val:",l[-2]),("Min val in list:",min(l)),("max val in list:",max(l))
print(fun([45,6,5,21,87]))