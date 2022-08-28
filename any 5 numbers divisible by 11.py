c=0
while True:
    num=int(input("Enter any number"))
    if(num%11==0):
        print(num)
        c=c+1
        if c==5:
            break
