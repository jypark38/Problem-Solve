t = int(input())
for _ in range(t):
    n = int(input())
    k = []
    a = []
    for i in range(2):
        k.append(list(map(int,input().split())))
        a.append([0]*n)

    a[0][0] = k[0][0]
    a[1][0] = k[1][0]
    if n == 1:
        print(max(a[0][0],a[1][0]))
        continue

    a[0][1] = a[1][0] + k[0][1]
    a[1][1] = a[0][0] + k[1][1]
    
    for j in range(2,n):
        a[0][j] = k[0][j] + max(a[1][j-2], a[1][j-1])
        a[1][j] = k[1][j] + max(a[0][j-2], a[0][j-1])
        
    print(max(a[0][n-1],a[1][n-1]))