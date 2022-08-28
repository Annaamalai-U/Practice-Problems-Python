a=0
b=1
l=[0,1]
for i in range(50): 
    c=a+b
    l.append(c)
    a=b
    b=c
print(l)
x=int(input("Enter the lower range in the Fibonacci series:"))
y=int(input("Enter the upper range in the Fibonacci series:"))
l2=[]
if (x not in l) or (y not in l):
    print("Your range elements or not in fibonacci series")
else:
    for i in l:
        if i>=x and i<=y:
            l2.append(i)
    print(l2)
