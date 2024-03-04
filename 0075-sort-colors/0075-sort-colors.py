class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        zeroIdx = 0
        pivot = 0
        twoIdx = len(nums)-1
        
        while pivot <= twoIdx:
            if(nums[pivot] == 0):
                nums[pivot] = nums[zeroIdx]
                nums[zeroIdx] = 0
                zeroIdx+=1
                pivot+=1
            elif(nums[pivot] == 2):
                nums[pivot] = nums[twoIdx]
                nums[twoIdx] = 2
                twoIdx -= 1
            else:
                pivot+=1
        print(nums)