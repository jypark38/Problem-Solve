n = int(input())

for i in range(1,n+1):
    str = ' '*(n-i)
    for j in range(1,2*i):
        if(i==n):
            str += '*'*(2*n-1)
            break
        if(j==1 or j==2*i-1):
            str+='*'
        else:
            str+=' '

    print(str)