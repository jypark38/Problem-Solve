class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums)-1
        
        while(l<r):
            p = (l+r)//2
            if(nums[p]<nums[p+1]):
                l = p+1
            if(nums[p]>nums[p+1]):
                r = p
        return l