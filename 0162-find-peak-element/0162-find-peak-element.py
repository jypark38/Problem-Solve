class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('-inf')]
        l = len(nums)
        if(l%2):
            p1 = l//2
            p2 = l//2
        else:
            p1 = l//2
            p2 = p1-1
        
        
        # print([float('inf')]+nums+[float('-inf')])
        
        while(p1<l+1 and p2>0):
            if(nums[p1]>nums[p1-1] and nums[p1]>nums[p1+1]):
                return p1-1
            if(nums[p2]>nums[p2-1] and nums[p2]>nums[p2+1]):
                return p2-1
            p1+=1
            p2-=1
                
            
        