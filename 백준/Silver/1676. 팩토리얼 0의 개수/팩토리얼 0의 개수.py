n = int(input())

fact = [1,1]

for i in range(2,n+1):
    fact.append(fact[-1]*i)

answer = 0
T = fact[n]
while T%10 == 0:
    answer+=1
    T = T//10
print(answer)
