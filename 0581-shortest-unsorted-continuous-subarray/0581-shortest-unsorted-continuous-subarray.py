class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        idx1 = 0
        idx2 = len(nums)-1
        minNum = 100001
        maxNum = -100001
#         최소값 구하기
        for i in range(len(nums)-1):
            if(nums[i] > nums[i+1]):
                if(nums[i+1] < minNum) :
                    minNum = nums[i+1]
                    idx1 = i+1
        for i in range(len(nums)-1,0,-1):
            if(nums[i] < nums[i-1]):
                if(nums[i-1] > maxNum) :
                    maxNum = nums[i-1]
                    idx2 = i-1
        print(idx1,minNum)
        print(idx2,maxNum)
        if(idx1 == 0 and idx2==len(nums)-1):
            return 0
        
        s = 0
        e = 0
        for i in range(idx1-1,-1,-1):
            if(nums[idx1]<nums[i]):
                s+=1
        for i in range(idx2+1,len(nums)):
            if(nums[idx2]>nums[i]):
                e+=1
        
        return s+e+idx2-idx1+1