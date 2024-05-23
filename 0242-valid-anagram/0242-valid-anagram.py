class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}
        
        if(len(s) != len(t)):
            return False
        
        for i in range(len(s)):
            c = s[i]
            if(c not in h):
                h[c] = 1
            else:
                h[c] += 1
        
        for c in t:
            if(c not in h):
                return False
            else:
                h[c] -= 1
                if(h[c] < 0):
                    return False
                
        return True