def plusMinus(arr):
    pos,neg,zero,tot=0,0,0,0
    tot=len(arr)
    for i in arr:
        if(i<0):
            neg=neg+1
        elif(i>0):
            pos=pos+1
        else:
            zero=zero+1
    print("""{:.6f}""".format(pos/tot))
    print("""{:.6f}""".format(neg/tot))
    print("""{:.6f}""".format(zero/tot))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)