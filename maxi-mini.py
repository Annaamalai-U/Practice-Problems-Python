def miniMaxSum(arr):
    mini=arr[0]
    maxi=arr[0]
    res=0
    for i in arr:
        res=res+i
        if(i<mini):
            mini=i
        if(i>maxi):
            maxi=i
    print(res-maxi," ",res-mini)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)