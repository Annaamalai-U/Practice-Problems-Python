def art(p):
    c=0
    for i in p.split(" "):
        if i.lower() in ["a","an","the"]:
            c+=1
    return(c)
p=input("Enter paragraph")
print(art(p))
print("\r")
