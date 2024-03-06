class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        c = intervals[0]
        answer = []
        for interval in intervals:
            if(c[1]<interval[0]):
                answer.append(c)
                c=interval
            else:
                if(c[1]<interval[1]):
                    c[1]=interval[1]
        answer.append(c)
                
        return answer
        