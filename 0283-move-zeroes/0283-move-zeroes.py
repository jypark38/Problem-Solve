class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx1 = 0
        idx2 = 0

        lenN = len(nums)

        while(idx2<lenN):
            if(nums[idx2] != 0):
                nums[idx1] = nums[idx2]
                idx1+=1            
            idx2+=1
        for i in range(idx1, lenN):
            nums[i]=0
            
        print(nums)