ph=[[1,"VIVO","Vivo T1 44W","RAM:",4,"GB","Storage:",128,"GB","Front Camera:",16,"MP","Back Camera-50MP + 2MP + 2MP","Price-₹",14499],
    [2,"XIAOMI","Redmi 10","RAM:",4,"GB","Storage:",64,"GB","Front Camera:",5,"MP","Back Camera-50MP + 2MP","Price-₹",10499],
    [3,"ONE PLUS","OnePlus Nord CE 2 5G","RAM:",8,"GB","Storage:",128,"GB","Front Camera:",16,"MP","Back Camera-64MP + 8MP + 2MP","Price-₹",23499],
    [4,"iQOO","iQOO Z6 Pro 5G","RAM:",6,"GB","Storage:",128,"GB","Front Camera:",16,"MP","Back Camera-64MP + 8MP + 2MP","Price-₹",23999],
    [5,"VIVO","Vivo T1","RAM:",4,"GB","Storage:",128,"GB","Front Camera:",16,"MP","Back Camera-50MP + 8MP + 2MP","Price-₹",16990],
    [6,"ONE PLUS","OnePlus Nord 2 x Pac-Man Edition","RAM:",12,"GB","Storage:",256,"GB","Front Camera:",32,"MP","Back Camera-50MP + 8MP + 2MP","Price-₹",37999],
    [7,"REALME","Realme Narzo 50A","RAM:",4,"GB","Storage:",64,"GB","Front Camera:",8,"MP","Back Camera-50MP + 2MP","Price-₹",11499],
    [8,"JIO","Jio Phone Next","RAM:",2,"GB","Storage:",16,"GB","Front Camera:",8,"MP","Back Camera-13MP","Price-₹",4619],
    [9,"INFINIX","Infinix Note 10 Pro","RAM:",8,"GB","Storage:",256,"GB","Front Camera:",16,"MP","Back Camera-64MP + 8MP + 2MP + 2MP","Price-₹",16999],
    [10,"SAMSUNG","Samsung W22 5G","RAM:",12,"GB","Storage:",256,"GB","Front Camera:",10,"MP","Back Camera-12MP + 12MP + 12MP","Price-₹",74270],
    [11,"SAMSUNG","Samsung Galaxy A33 5G","RAM:",6,"GB","Storage:",128,"GB","Front Camera:",13,"MP","Back Camera-48MP + 8MP + 5MP + 2MP","Price-₹",25999],
    [12,"ONEPLUS","OnePlus 10R 5G","RAM:",12,"GB","Storage:",256,"GB","Front Camera:",16,"MP","Back Camera-50MP + 8MP + 2MP","Price-₹",38999],
    [13,"SAMSUNG","Samsung Galaxy M52 5G","RAM:",6,"GB","Storage:",128,"GB","Front Camera:",32,"MP","Back Camera-64MP + 12MP + 5MP","Price-₹",24999],
    [14,"XIAOMI","Redmi Note 11 Pro","RAM:",6,"GB","Storage:",64,"GB","Front Camera:",16,"MP","Back Camera-108MP + 8MP + 2MP + 2MP","Price-₹",18999],
    [15,"GOOGLE","Google Pixel 4a","RAM:",6,"GB","Storage:",128,"GB","Front Camera:",8,"MP","Back Camera-12.2MP","Price-₹",32399]]
print("#price details of a given model....")
for i in ph:
    print(i[2])
print("-"*120)
model=input("Enter the Phone model:")

for i in ph:
    if i  in ph:
        if model==i[2]:
            print(i[13],i[14])
    if i not in ph:
            print("Please Enter the correct model name")
print("-"*120)
print("#Brands in Alphabetical order....")
order=[]
for i in ph:
    order.append(i[2])

for i in range(len(order)):
    for j in range(i+1,len(order)):
        if order[i]>order[j]:
            order[i],order[j]=order[j],order[i]
for i in order:
    print(i)
print("-"*120)
print("# highest resolution front camera....")
cam=[]
for i  in ph:
    cam.append(i[10])
a=max(cam)
print(a,"MP")
print("-"*120)
print("#mobile phone details greater than the given RAM value....")
ram=int(input("Enter the RAM Specification:"))
j=1
for i in ph:
    if i[4]>=ram:
        print(j,".",i[2],"|","RAM:",i[4],"GB","|","STORAGE:",i[7],"GB","|","FRONT CAMERA:",i[10],"MP","|","REAR CAMERA",i[12],"|","PRICE-₹",i[14])
        j+=1
print("-"*120)
print("#mobile phone details of the given brand with a sorted price order....")
for i in range(len(ph)):
    for j in range(i+1,len(ph)):
        if ph[i][-1]>ph[j][-1]:
            ph[i],ph[j]=ph[j],ph[i]
k=1
for i in ph:
    print(k,".",i[2],"|","RAM:",i[4],"GB","|","STORAGE:",i[7],"GB","|","FRONT CAMERA:",i[10],"MP","|","REAR CAMERA",i[12],"|","PRICE-₹",i[14])
    k+=1
