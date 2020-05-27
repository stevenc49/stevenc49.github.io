x = 1
y = 3


tmp = x ^ y

count=0
while tmp>0:
    if tmp&1==1:
        count+=1
    tmp>>=1


print( count )