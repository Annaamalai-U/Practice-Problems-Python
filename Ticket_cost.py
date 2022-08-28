print("Total number of Queen Seats:300 Total Number of King Seats:300")
print("Cost of one Queen Seat:Rs120 Cost of one King Seat:Rs.150")
a=int(input("Is it Houseful(1/0):"))
if a!=1 and a!=0:
    print("Please only Enter 0 or 1")
else:
    if a==1:
        tot_cost=(300*120)+(300*150)
        print("The total TICKET AMOUNT COLLECTED:",tot_cost)
    else:
        Q=int(input("Enter the Percentage of Queen Seats filled:"))
        K=int(input("Enter the Percentage of King Seats filled:"))
        if Q>100 or K>100:
            if Q>100:
                print("The percentage of Queen seats should be less than or equal to 100, please ensure the entry")
            if K>100:
                print("The percentage of King seats should be less than or equal to 100, please ensure the entry")
        else:
            seat_Q=(Q/100)*300
            seat_K=(K/100)*300
            cost_Q=seat_Q*120
            cost_K=seat_K*150
            tot=cost_Q+cost_K
            print("The total TICKET AMOUNT COLLECTED:",tot)
