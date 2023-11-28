l = [-1]*(ord('z')-ord('a')+1)

s = input()
for i in range(len(s)):
    if(l[ord(s[i])-ord('a')] == -1):
        l[ord(s[i])-ord('a')] = i

print(*l)