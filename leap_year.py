def leap_year(year):
    if(year%4!=0):
        print("False");
    else:
        if(year%100==0 and year%400!=0):
            print("False")
        else:
            print("True")
n=int(input(""))
leap_year(n)
