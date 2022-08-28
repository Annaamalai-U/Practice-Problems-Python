#1.Area of the circle
r=int(input("Enter the Radius of the circle:"))
area=0
if r<0:
    print("Invlid Input")
else:
    print("The area of the circle:",3.14*r*r)

#2.Weight Conversion    
p=int(input("Enter the Weight in KGs:"))
if p<0:
    print("Invalid Input")
else:
    print("The correponding Weight in Pounds:",p*2.2)
    
cm=int(input("Enter the length in CM:"))
if cm<0:
    print("Invalid Input")
else:
    print("The corresponding length in Feets:",0.0328*cm)

#3.Leap Year
y=int(input("Enter the Year:"))
if y<0:
    print("Invalid input")
elif ((y%4==0) and (y%400==0 or y%100!=0)):
    print(y," is a leap year")
else:
    print(y," is not a leapyear")

#4.Operator
a=int(input("Enter num1:"))
b=int(input("Enter num2"))
c=input("Enter the Operator:")
if (c=='+' or c=='-' or c=='*' or c=='/' or c=='%'):
    if c=='+':
        print("The sum of 2 numbers:",a+b)
    elif c=='-':
        print("The difference of 2 numbers:",a-b)
    elif c=='*':
        print("The product of 2 numbers:",a*b)
    elif c=='/':
        print("The quotient of 2 numbers:",a//b)
    elif c=='%':
        print("The reminder of 2 numbers:",a%b)
else:
    print("Invalid operator")

#5.BMI Value
h=float(input("Enter Your height in Metres:"))
w=float(input("Enter your weight in Kgs:"))
bmi=0
if(h>=0 and w>=0):
    bmi=w/(h*h)
    print("Your BMI Value is:",round(bmi,2))
    if(bmi<18.5):
        print("You are Under Weight")
    elif(bmi>=18.5 and bmi<24.5):
        print("You are in normal weight")
    else:
        print("You are in Over weight")
elif(h<0 or w<0):
    if (h<0 and w>0):
        print("Length cannot be negative")
    elif (w<0 and h>0):
        print("Weight cannot be negative")
    else:
        print("Length and Weight cannot be negative")

#6.Quadrant
m=input("Enter the Month:")
if (m=="jan" or m=="feb" or m=="mar"):
    print("1st Quadrant")
elif (m=="april" or m=="may" or m=="june"):
    print("2nd Quadrant")
elif (m=="july" or m=="aug" or m=="sep"):
    print("3rd Quadrant")
elif (m=="oct" or m=="nov" or m=="dec"):
    print("4th Quadrant")
else:
    print("Invalid Month")

#7.time conversion
time=int(input("Enter the time:"))
if(time>=0 and time<24):
    if(time>0 and time<12):
        print(time,"AM")
    elif(time>12 and time<24):
        print(time-12,"PM")
    elif(time==0):
        print("12AM")
    elif(time==12):
        print("12PM")
else:
    print("Invalid Time")

#8.area of a rectangular land

diameter=int(input("Enter the diameter of the Circular pond:"))
length=int(input("Enter the length of the Reactangular Land:"))
breadth=int(input("Enter the Breatdth of the Rectangular Land:"))
aoc=0
aor=0
ra=0
if (diameter<length and diameter<breadth):
    radius=diameter/2
    aoc=3.14*radius*radius
    aor=length*breadth
    ra=aor-aoc
    print("Area of the Circular pond:",aoc,"m^2")
    print("Area of the Rectangular land:",aor,"m^2")
    print("The remaining Area:",ra,"m^2")
elif(diameter>=length or diameter>=breadth):
    if(diameter>=length and diameter<breadth):
        print("Diameter cannot be greater than the length of the land")
    elif(diameter<length and diameter>=breadth):
        print("Diameter cannot be greater than the breadth of the land")
    else:
        print("Diameter cannot be greater than both length and breadth of the rectangular land")

#9.simple interest
principal=int(input("Enter the Principal Amount:"))
years=int(input("Enter the No.of.Years:"))
interest=int(input("Enter the Rate of Interest:"))
si=0
if(principal>=0 and years>=0 and interest>=0):
    si=(principal*years*interest)/100
    print("The total interest:",si)
elif(principal<0 or years<0 or interest<0):
    if(principal<0 or years<0 and interest>0):
        if(principal<0 and years>0):
            print("Principal amount cannot be negative")
        elif(principal>0 and years<0):
            print("Total No.of.Years cannot be negative")
        else:
            print("Principal amount and the total no.of.years cannot be negative")
    elif(principal>0 and years<0 or interest<0):
        if(interest<0 and years>0):
            print("Interest rate cannot be negative")
        elif(interest>0 and years<0):
            print("Total No.of.Years cannot be negative")
        else:
            print("Interest rate and the total no.of.years cannot be negative")
    elif(principal<0  or interest<0 and years>0):
        if(principal<0 and interest>0):
            print("Principal amount cannot be negative")
        elif(principal>0 and interest<0):
            print("Rate of interest cannot be negative")
        else:
            print("Principal amount and the Interest Rate cannot be negative")
    else:
        print("Principal Amount,Rate of Interest and Total No.of.Years cannot be negative")

#10.cm to feet and inches:
cm=int(input("Enter the Centimeter:"))
if(cm>=0):
    feet=cm*0.0328
    inches=cm*0.393
    print("The corresponding feet:",round(feet,2),"feet")
    print("The corresponding inch:",round(inches,2),"inch")
else:
    print("Length cannot be negative")
