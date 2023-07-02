import math
q = int(input().strip())
for q_itr in range(q):
    n = int(input().strip())
    a = []
    for _ in range(2 * n):
        a.append(list(map(int, input().rstrip().split())))
    v = 0
    for i in range(n):
        for j in range(n):
            l = []
            l.append(a[i][j]) # current matrix
            l.append(a[2 * n - 1 - i][j])  # bottom left
            l.append(a[i][2 * n - 1- j]) # top right
            l.append(a[2* n - 1 - i][2 * n - 1- j]) # bottom right
            maxv = max(l)
            v += maxv
print(l)
print(v)