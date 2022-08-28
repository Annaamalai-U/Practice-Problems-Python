print("SJF")
n=int(input("ENTER no. of processes "))
i=0
L=[]
d1={}
dw={}
sum1=0
sum2=0
p=0
while i<n:
    b=int(input("Enter process time {} ".format(i+1)))
    a=int(input("Enter arrival time {} ".format(i+1)))
    L.append(a)
    d1[i+1]=b
    sum2=sum2+b
    i+=1
    a = dict(sorted(d1.items(), key=lambda x: x[1]))
for j in a.keys():
    dw[j]=p
    p+=a[j]
for u in dw.keys():
    print("WAITING TIME FOR Process",u,"=",dw[u]+min(L))
    sum1+=dw[u]
print("AVG WAITING TIME",round(sum1/n,2))
print("TOTAL BURST TIME",sum2)
print("TOTAL THROUGHPUT",n/sum2)
