def countingSort(arr):
    n=len(arr)
    freq=[]
    for i in range(n):
        freq.append(0)
    for i in arr:
        freq[i]+=1
    count=0
    if(n>100):
        for i in range(n-1,0,-1):
            if freq[i]==0:
                count+=1
            else:
                break
    last=n-count
    freq=freq[0:last]
    return freq
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    for i in result:
        print(i,end=" ")
