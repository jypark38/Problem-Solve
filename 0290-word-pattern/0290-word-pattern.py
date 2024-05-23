class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h = {}
        
        arrS = s.split(' ')
        
        if(len(pattern) != len(arrS)):
            return False
        
        for i in range(len(pattern)):
            c = pattern[i]
            
            if(c not in h):
                if(arrS[i] in h.values()):
                    return False
                h[c] = arrS[i]
            else:
                if(h[c] != arrS[i]):
                    return False
            
                
            
        return True