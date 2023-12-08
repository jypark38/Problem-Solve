n = int(input())

arr = [0] + list(map(int,input().split()))
d = [0 for _ in range(n+1)]
d[1] = arr[1]
for i in range(2,n+1):
    if d[i-1]+arr[i]<arr[i]:
        d[i] = arr[i]
    else:
        d[i] = d[i-1]+arr[i]
print(max(d[1:]))