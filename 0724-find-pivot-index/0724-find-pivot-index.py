class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i in range(0,len(nums)):
            total -= nums[i]
            if(i != 0):
                left += nums[i-1]
            if(left == total):
                return i
        return -1