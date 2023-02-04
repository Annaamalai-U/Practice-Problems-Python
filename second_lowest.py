n=int(input())
L=[]
for i in range(0,n):
    l=[]
    name=input()
    mark=float(input())
    l.append(name)
    l.append(mark)
    L.append(l)
marks = sorted([L[i][1] for i in range(len(L))], reverse = True)
marks=list(set(marks))
temp=marks[-2]
second_top = [L[i] for i in range(len(L)) if L[i][1] == temp]
second_top.sort()
for i in second_top:
    print(i[0])
    
