def pali(p):
    for i in p.split(" "):
        c=0
        for j in range(len(i)):
            if i[j]==i[len(i)-j-1]:
                c+=1
                if c==len(i):
                    print(i)
p=input("Enter paragraph")
pali(p)
print("\r")
