# Count an perticular charactor.
#here "t" is  the 2 chars in a given string
def fun(s):
    count=0;
    for i in s:
        if (i=="t"):
            count=count+1
        print(count,end=" ")
    return s
fun(s="hiii hat ant rare")