def diagonalDifference(arr):
    n=len(arr)
    d1,d2=0,0
    y=n-1
    for i in range(n):
        for j in range(n):
            if(i==j):
                d1=d1+arr[i][j]
            if(j==y):
                d2=d2+arr[i][j]
        y-=1
    print(abs(d1-d2))
if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    diagonalDifference(arr)
