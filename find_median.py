def findMedian(arr):
    x=sorted(arr)
    n=len(x)
    mid=n//2
    print(x[mid])
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    findMedian(arr)