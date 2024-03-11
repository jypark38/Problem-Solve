class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)-len(needle)+1):
            cnt = 0
            for j in range(len(needle)):
                if(haystack[i+j] != needle[j]): break
                cnt+=1
            
            if(cnt==len(needle)): return i
            
        return -1