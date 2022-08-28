m=input("Enter Month in the way 1st letter capital followed by small letters")
ml=["January","February","March","April","May","June","July","August","September","October","November","December"]
if m in ml:
    if m in ml[0:3] :
        print("The month ",m," is in 1st Quadrant")
    elif m in ml[3:6] :
        print("The month ",m," is in 2nd Quadrant")
    elif m in ml[6:9] :
        print("The month ",m," is in 3rd Quadrant")
    else:
        print("The month ",m," is in 4th Quadrant")
else:
    print("Other Values NOT Allowed")
