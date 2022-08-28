def end(p,ch):
    flag=0
    for i in p.split(" "):
        if i[-1]==ch:
            print(i)
            flag=1
    if flag!=1:
        print("NO WORD FOUND")
p=input("Enter paragraph")
ch=input("Enter character (last char)")
end(p,ch)
print("\r")
