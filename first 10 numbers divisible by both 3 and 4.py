n=1
i=1
while True:
    if(n%3==0 and n%4==0):
        print(n)
        n=n+1
        i=i+1
        if(i==21):
            break
    else:
        n=n+1
