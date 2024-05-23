class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        
        for n in nums:
            if(n not in h):
                h[n] = 1
            else:
                h[n] += 1
                
        sorted_dict = sorted(h.items(), key= lambda item:item[1], reverse=True)
        answer = []
        
        for i in range(k):
            answer.append(sorted_dict[i][0])
        return answer