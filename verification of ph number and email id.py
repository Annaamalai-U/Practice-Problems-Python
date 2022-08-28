def ph():
    no=int(input("Enter your phone number:+91 "))
    b=str(no)
    if len(str(no))==10 and b[0] in "6789":
        print("Your number is verified!!!!")
    else:
        if len(str(no))<10 or len(str(no))>10:
            print("Phone number should contain exactly 10 digits!!!")
        if b[0] not in "6789":
            print("Phone number should start with only 6,7,8 or 9")
def mail():
    mail=input("Enter your e-mail id:")
    if mail in "@.comedu":
        print("Your mail id is Verified!!!")
    else:
        print("please enter a valid e-mail id!!!")
ph()
mail()
