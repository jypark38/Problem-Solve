class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        s = intervals[0][0]
        e = intervals[0][1]
        answer = []
        for i in range(1,len(intervals)):
            if(e<intervals[i][0]):
                answer.append([s,e])
                s=intervals[i][0]
                e=intervals[i][1]
            else:
                if(e<intervals[i][1]):
                    e=intervals[i][1]
        answer.append([s,e])
                
        return answer
        