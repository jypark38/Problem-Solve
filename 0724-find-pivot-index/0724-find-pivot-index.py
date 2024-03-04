class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        idx = -1
        for i in range(0,len(nums)):
            total -= nums[i]
            if(i != 0):
                left += nums[i-1]
            if(left == total):
                idx = i
                break
        return idx