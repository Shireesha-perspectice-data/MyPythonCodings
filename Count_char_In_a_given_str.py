#Count charactors in a given string.   
#samp="hiz thhis the python explanation and DataScience z"
def fun(samp):
    return ([{each:samp.count(each) for each in samp}])
print(fun(samp="hiz thhis the python explanation and DataScience z"))
