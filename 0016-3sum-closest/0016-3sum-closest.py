class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer = float('inf')
        md = float('inf')
        
        nums.sort()
        
        if(len(nums)==3):
            return sum(nums)
        
        
        for i in range(len(nums)-2):
            
            l = i+1
            r = len(nums)-1
            
            while(l<r):
                s = nums[i]+nums[l]+nums[r]
                d = target-s
                if(md>abs(d)):
                    md = abs(d)
                    answer = s
                if(s<target):
                    l+=1
                elif(target<s):
                    r-=1
                else:
                    return s
        
        return answer