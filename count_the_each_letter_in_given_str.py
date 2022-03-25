def fun(sam):
    d={}
    for j in sam:
        if j in d:
            d[j]+=1
        else:
            d[j]=1
    return d
print(fun(sam="Data Science"))