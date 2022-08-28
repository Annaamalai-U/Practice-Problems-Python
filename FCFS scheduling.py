print("FCFS")
n=int(input("ENTER no. of processes"))
i=1
dw={}
sum1=0
sum2=0
p=0
while i<=n:
    b=int(input("Enter process time"))
    sum2+=b
    dw[i]=p
    i+=1
    p+=b
for j in dw.keys():
    print("WAITING TIME FOR Process",j,"=",dw[j])
    sum1+=dw[j]
print("AVG WAITING TIME",round(sum1/n,2))
print("TOTAL BURST TIME",sum2)
print("TOTAL THROUGHPUT",sum2/n)
