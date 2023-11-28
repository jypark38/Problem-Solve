alp = {}

for i in range(ord('a'),ord('z')+1):
    alp[chr(i)] = 0

s = input()
for c in s:
    alp[c] += 1
answer = [str(i) for i in list(alp.values())]
print(' '.join(answer))