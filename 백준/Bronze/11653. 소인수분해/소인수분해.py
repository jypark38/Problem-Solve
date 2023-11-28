import math
n = int(input())

while n>1:
    tmp = 2
    flag = 0
    # while n%tmp != 0 and tmp < round(math.sqrt(n))+1:
    while True:
        if(n%tmp==0):
            flag = 1
            break
        if(tmp>=round(math.sqrt(n))+1):
            flag=2
            break
        tmp+=1
    if flag == 1:
        n = n//tmp
        print(tmp)
    if flag == 2:
        print(n)
        break
    