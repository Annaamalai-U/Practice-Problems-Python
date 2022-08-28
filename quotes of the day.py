def quote(day):
    if day.upper()=="MON":
        return("MARVELLOUS MONDAY")
    elif day.upper()=="TUE":
        return("THOUGHTFUL TUESDAY")
    elif day.upper()=="WED":
        return("WHOLESOME WEDNESDAY")
    elif day.upper()=="THU":
        return("TRENDY THURSDAY")
    elif day.upper()=="FRI":
        return("FULFILLED FRIDAY")
    elif day.upper()=="SAT":
        return("SATIRE SATURDAY")
    elif day.upper()=="SUN":
        return("SUPER SUNDAY")
    else:
        return("Invalid format")
day=input("Enter day in 3 word format like mon,tue etc.,")
print(quote(day))
