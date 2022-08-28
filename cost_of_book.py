amount=int(input("Enter the Cost of the Book:"))
if amount<0:
    print("The amount cannot be negative,please enter a correct amount")
else:
    profit=(12/100)*amount
    cgst=(9/100)*amount
    sgst=(9/100)*amount
    tot=amount+profit+cgst+sgst
    print("The profit to the Shopkeeper:",round(profit,2))
    print("The CGST for the product:",round(cgst,2))
    print("The SGST for the product:",round(sgst,2))
    print("The total amount of the product inclusive of all taxes:",round(tot,2))
