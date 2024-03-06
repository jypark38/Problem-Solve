class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        c = intervals[0]
        answer = []
        for i in range(1,len(intervals)):
            if(c[1]<intervals[i][0]):
                answer.append(c)
                c=intervals[i]
            else:
                if(c[1]<intervals[i][1]):
                    c[1]=intervals[i][1]
        answer.append(c)
                
        return answer
        