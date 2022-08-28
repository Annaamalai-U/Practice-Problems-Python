i=int(input("Enter first number"))
j=int(input("Enter second number"))
o=input("Enter a operator +-*/%")
if o in "+-*/%":
    if o=="+":
        print("Addition of ",i," and",j," = ",i+j)
    elif o=="-":
        print("Subraction of ",i," and",j," = ",i-j)
    elif o=="*":
        print("Multiplication of ",i," and",j," = ",i*j)
    elif o=="/":
        print("Division of ",i," and",j," = ",i/j)
    elif o=="%":
        print("Modulo division of ",i," and",j," = ",i%j)
else:
    print("Only the Above values should be written")
