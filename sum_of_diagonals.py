n=int(input("Enter the order of square matrix:"))
m=[]
for i in range(0,n):
    mr=[]
    for j in range(0,n):
        a=int(input("Enter the {}th and {}th element:".format(i+1,j+1)))
        mr.append(a)
    m.append(mr)
s1=0
s2=0
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            s1=s1+m[i][j]
k=(n-1)
for i in range(0,n):
    for j in range(0,n):
        if j==k:
            s2=s2+m[i][j]
            if i==j:
                s2=s2-m[i][j]
            k-=1
print("The sum of the principal diagonal is:",s1)
print("The sum of the other diagonal excluding the common element is:",s2)
