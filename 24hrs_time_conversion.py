def timeConversion(s):
    time=s.split(":")
    if("AM" in time[2]):
        sub=time[2].split('A')
        if(time[0]=="12"):
            return "00:"+str(time[1])+":"+sub[0]
        else:
            return str(time[0])+":"+str(time[1])+":"+sub[0]
    if("PM" in time[2]):
        sub=time[2].split('P')
        if(time[0]=="12"):
            return "12:"+str(time[1])+":"+sub[0]
        else:
            return str(int(time[0])+12)+":"+str(time[1])+":"+sub[0]

if __name__ == '__main__':
    s=input()
    ans=timeConversion(s)
    print(ans)
