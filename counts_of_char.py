# count the charactors of
sample="i wants to reason ,why do you like this activities,can i know the reason.iam here...."
d={}
for j in sample:
    if j in d:
        d[j]+=1
    else:
        d[j]=1
print(d)
        
