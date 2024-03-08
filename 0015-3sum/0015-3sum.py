class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        s = set()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            if(nums[i] > 0):
                break
            while(l<r):
                tmp = nums[i]+nums[l]+nums[r]
                if(tmp<0):
                    l+=1
                elif(tmp>0):
                    r-=1
                else:
                    t = (nums[i],nums[l],nums[r])
                    if t not in s:
                        s.add(t)
                        answer.append(t)
                    l+=1
                    r-=1
        
        return answer
       