n,b = map(int,input().split())
answer =''
while n>0:
    n,t = divmod(n,b)
    if(t>=10):
        t = chr(t+55)
    answer = str(t) + answer
print(answer)