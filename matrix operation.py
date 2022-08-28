m1=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
m2=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#m1=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
#m1=[[0,0,0],[0,0,0],[0,0,0]]
#addition of matrix 
rowadd=[]
addm=[]
avg=[]
for i in range(0,len(m1)):
    for j in range(0,len(m1[i])):
        add=m1[i][j]+m2[i][j]
        rowadd.append(add)
    addm.append(rowadd)
    rowadd=[]
print(addm)

#subraction of matrix
rowadd=[]
addm=[]
for i in range(0,len(m1)):
    for j in range(0,len(m1[i])):
        add=m1[i][j]-m2[i][j]
        rowadd.append(add)
    addm.append(rowadd)
    rowadd=[]
print(addm)

#multipilcation of matrix

mrlist=[]
rlist=[]
m=len(m1)
n=len(m1[i])
o=len(m1[i])
for i in range(0,m):
    for j in range(0,n):
        for k in range(0,o):
            add=add+m1[i][k]*m2[k][j]
        rlist.append(add)
        add=0
    mrlist.append(rlist)
    rlist=[]
print(mrlist)

#diagonal greatest element

big=m1[0][0]
rowlen=len(m1[0])
for i in range(0,len(m1)):
    for j in range(0,len(m1[i])):
        if(i==j):
            if(big<m1[i][j]):
                big=m1[i][j]
        elif(j+1==rowlen):
            if(big<m1[i][j]):
                big=m1[i][j]
            rowlen-=1
print(big)

#avg and multipliaction of each row and column


for i in range(0,len(m1)):
    sr=0
    sc=0
    mr=1
    mc=1
    for j in range(0,len(m1[i])):
        sr=sr+m1[i][j]
        sc=sc+m1[j][i]
        mr=mr*m1[i][j]
        mc=mc*m1[j][i]
    print("the product of row ",i+1,"is ",mr)
    print("the product of column ",i+1,"is ",mc)
    print("the average of row ",i+1,"is ",sr/4)
    print("the average of column ",i+1,"is ",sc/4)

#identity matrix

maindiagonal=[]
c=0
d=0
for i in range(0,len(m1)):
    for j in range(0,len(m1[i])):
        if(i==j):
            maindiagonal.append(m1[i][j])
        else:
            if(m1[i][j]!=0):
                c+=1
mvalue=maindiagonal[0]
for z in range(0,len(maindiagonal)):
    if(mvalue!=maindiagonal[z]):
        d+=1
if(c>0 or d>0):
    print("not identity matrix")
else:
    print("identity matrix")

#magic square

mlist=[]
md1=0
md2=0
for i in range(0,len(m1)):
    sr=0
    sc=0
    for j in range(0,len(m1[i])):
        sr=sr+m1[i][j]
        sc=sc+m1[j][i]
        if(i==j):
            md1=md1+m1[i][j]
        if(j+1==len(m1[i])):
            md2=md2+m1[i][j]
    mlist.append(sr)
    mlist.append(sc)
mlist.append(md1)
mlist.append(md2)
f=0
magic=mlist[0]
for z in range(0,len(mlist)):
    if(magic!=mlist[z]):
        f+=1
if(f>0):
    print("not magic sqaure")
else:
    print("magic sqaure")
