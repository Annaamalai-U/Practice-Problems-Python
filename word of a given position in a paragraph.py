def wordpos(p,pos):
    L=p.split(" ")
    if pos <= len(L):
        print(L[pos-1])
    else:
        print("Index out of range")
p=input("Enter paragraph")
pos=int(input("Enter position"))
wordpos(p,pos)
print("\r")
