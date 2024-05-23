class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h = {}
        
        for i in range(len(s)):
            if(s[i] not in h):
                if(t[i] in h.values()):
                    return False
                h[s[i]] = t[i]
                continue
            if(h[s[i]] != t[i]):
                return False
            
        return True