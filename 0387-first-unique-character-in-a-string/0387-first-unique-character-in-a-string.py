class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = {}
        for i in range(len(s)):
            c = s[i]
            if(c not in h):
                h[c] = 1
            else:
                h[c]+=1
        
        for i in range(len(s)):
            c = s[i]
            if(h[c] == 1):
                return i
        
        
        return -1