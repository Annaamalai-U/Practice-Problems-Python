'i=input("Enter time in 24 hour using this : ")
l=i.split(":")
for j in l:
    if len(j)==1:
        u="0"+j
        l[l.index(j)]=u
print(l)
if (int(l[0])<=24 and int(l[0])>=0 and int(l[1])>=0 and int(l[1])<=60 and int(l[2])>=0 and int(l[2])<=60):
    if(int(l[0])<=12):
        print("Time in 12 hour ",i," A.M")
    else:
        print("Time in 12 hour ",int(l[0])-12,":",l[1],":",l[2]," P.M")
else:
    print("Time should be in crt format")
