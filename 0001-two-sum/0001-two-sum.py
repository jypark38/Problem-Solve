class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         for i in range(len(nums)):
#             nums[i] = [nums[i],i]

        if(len(nums)==2):
            return [0,1]
        
        nums = list(enumerate(nums))
        nums.sort(key=lambda x:x[1])
        
        print(nums)
        l = 0
        r = len(nums)-1
        
        while(nums[l][1]+nums[r][1] != target):
            if(nums[l][1]+nums[r][1]>target):
                r-=1
            if(nums[l][1]+nums[r][1]<target):
                l+=1
        
        return [nums[l][0],nums[r][0]]
        