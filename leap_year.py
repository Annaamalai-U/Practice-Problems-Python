y=int(input("Enter an Year to check leap year or not"))
if(len(str(y))==4 and str(y)[0]!=0):
    if((y%400==0 or y%100!=0) and (y%4==0)):
        print("Leap Year")
    else:
        print("Non Leap Year")
else:
    print("Year should be of 4 values")
