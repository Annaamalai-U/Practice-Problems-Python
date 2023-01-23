pairs=int(input())
L=[]
for i in range(0,pairs):
    l=[]
    x=int(input())
    y=int(input())
    l.append(x)
    l.append(y)
    L.append(l)
val=[]
val2=[]
for i in L:
    val.append(abs(i[1]-i[0]))
for i in range(len(L)-1):
    if(L[i][1]>L[i+1][0]):
        val2.append(abs(L[i][1]-L[i+1][0]))
sum1=0
sum2=0
for i in val:
    sum1=sum1+i
for i in val2:
    sum2=sum2+i
dist=sum1-sum2
print(dist)
