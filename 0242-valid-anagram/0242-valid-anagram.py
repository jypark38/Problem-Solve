class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h_s = {}
        h_t = {}
        
        if(len(s) != len(t)):
            return False
        
        for i in range(len(s)):
            c_s = s[i]
            c_t = t[i]
            
            if(c_s not in h_s):
                h_s[c_s] = 1
            else:
                h_s[c_s] += 1
            if(c_t not in h_t):
                h_t[c_t] = 1
            else:
                h_t[c_t] += 1
            
        for c_s in h_s:
            if(c_s not in h_t):
                return False
            elif (h_s[c_s] != h_t[c_s]):
                return False
            
        return True