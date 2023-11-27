n,b = input().split()
b = int(b)
n = n[::-1]
answer = 0

for i in range(0,len(n)):
    if(ord(n[i])>=65):
        result = pow(b,i)*(ord(n[i])-55)
    else:
        result = pow(b,i)*int(n[i])

    answer += result

print(answer)