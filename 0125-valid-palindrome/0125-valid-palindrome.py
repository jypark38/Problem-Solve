class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        
        start = 0
        end = len(s)-1
        
        while(end>=start):
            while start < len(s)-1 and not ('a' <= s[start] <= 'z' or '0'<= s[start]<='9'):
                start+=1
            while end >= 0 and not ('a' <= s[end] <= 'z' or '0' <= s[end] <= '9'):
                end -= 1
            if(s[start] != s[end]):
                print(s[start], s[end])
                return False
            start += 1
            end -= 1
            
                
        return True