count=0
while True:
    num1=int(input("Enter a 3 Digit Number:"))
    num1=str(num1)
    if(len(num1)==3):
        num1=int(num1)
        if(num1%10==num1//100):
            print(num1)
            count+=1
        if count==10:
            break
    else:
        print(" Please Enter a 3 Digit Number")
