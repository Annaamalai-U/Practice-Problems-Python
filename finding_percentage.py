n=int(input())
my_dict={}
for i in range(n):
    data=input()
    arr=data.split(" ")
    key=arr[0]
    marks=[arr[1],arr[2],arr[3]]
    my_dict.update({key:marks})
qname=input()
avg_arr=my_dict[qname]
avg=0
for i in avg_arr:
    avg=avg+float(i)
avg=float(avg/3)
avg='{0:.2f}'.format(avg)
print(avg)
