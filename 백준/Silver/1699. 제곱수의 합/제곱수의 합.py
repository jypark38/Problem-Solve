n = int(input())

a = [100001]*(n+1)

for i in range(1,n+1):
    s = int(i**(0.5))
    if s**2 == i:
        a[i] = 1
    else:
        for j in range(1,s+1):
            a[i] = min(a[i],a[i-j**2]+1)
            #어차피 a[s**2] = 1

print(a[n])
