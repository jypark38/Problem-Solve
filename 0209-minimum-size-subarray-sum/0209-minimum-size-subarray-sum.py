class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        
        s = 0
        e = 0
        subSum = 0
        
        length = len(nums)
        
        answer = 10**5 + 1
        
        while e < length:
            subSum += nums[e]
            e+=1
            
            while target <= subSum:
                l = e-s
                answer = min(answer,l)
                subSum -= nums[s]
                s+=1
            
        return answer if answer != 10**5+1 else 0