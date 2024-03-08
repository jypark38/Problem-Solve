class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        arr = sorted(nums)
        
        answer = set()
        
        for i in range(len(arr)-3):
            if(i>0 and arr[i] == arr[i-1]):
                continue
            for j in range(i+1,len(arr)-2):
                if(j>i+1 and arr[j] == arr[j-1]):
                    continue
                n1 = arr[i]
                n2 = arr[j]
                l = j+1
                r = len(arr)-1
                
                while(l<r):
                    res = n1+n2+arr[l]+arr[r]
                    if(target==res):
                        answer.add((n1,n2,arr[l],arr[r]))
                        l+=1
                        r-=1
                    elif(res<target):
                        l+=1
                        while(l<r and arr[l] == arr[l-1]):
                            l+=1
                    else:
                        r-=1
                        while(l<r and arr[r] == arr[r+1]):
                            r-=1
        return list(answer)