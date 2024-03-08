class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer = 0
        md = float('inf')
        
        nums.sort()
        
        if(len(nums)==3):
            return sum(nums)
        
        for i in range(len(nums)-2):
            
            l = i+1
            r = len(nums)-1
            
            while(l<r):
                s = nums[i]+nums[l]+nums[r]
                if(md>abs(target-s)):
                    md = abs(target-s)
                    answer = s
                if(s<target):
                    l+=1
                elif(s>target):
                    r-=1
                else:
                    return s
        
        return answer