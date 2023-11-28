import math
n,m = map(int,input().split())

for i in range(n,m+1):
    if i == 1: continue
    flag = 0
    for j in range(2,round(math.sqrt(i))+1):
        if(i%j==0):
            flag = 1
            break
    if flag==0:
        print(i)