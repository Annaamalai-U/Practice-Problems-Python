set1={2,3,4}
set2={2,3,4,5}
uset=set()
iset=set()
dset=set()
c=0

#add

set1.add(5)

#union

for i in set1:
    uset.add(i)
for j in set2:
    uset.add(j)
print(uset)

#intersection and disjoint

for i in set1:
    for j in set2:
        if(i==j):
            iset.add(j)
print(iset)
if(len(iset)==0):
    print("set1 and set2 are disjoint sets")
else:
    print("set1 and set2 are not disjoint sets")

#difference

for i in set1:
    if(i not in set2):
        dset.add(i)
for j in set2:
    if(j not in set1):
        dset.add(j)
print(dset)

#subset and superset

for i in set2:
    if(i not in set1):
        c=c+1
if(c>0):
    print("set2 is not a subset of set1")
else:
    print("set2 is a subset of set1")
    print("set1 is a superset of set2")
    if(len(set1)==len(set2)):
        print("set1 is also a subset of set2")
        print("set2 is also superset of set1")

#remove an item in the set

set1.discard(int(input("enter a number to remove from the set")))
print(set1)
