n = int(input())

fact = [1,1]

for i in range(2,n+1):
    fact.append(fact[-1]*i)

print(fact[n])