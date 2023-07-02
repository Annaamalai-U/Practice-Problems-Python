def lonelyinteger(a):
    tot1,tot2=0,0
    s=list(set(a))
    for i in a:
        tot1=tot1+i
    for i in s:
        tot2=tot2+i
    tot2=2*tot2
    print(abs(tot1-tot2))
if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    lonelyinteger(a)
