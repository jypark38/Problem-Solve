def solution(score):
    answer = []
    mean = []
    for e,m in score:
        mean.append((e+m)/2)
    for i in range(len(mean)):
        rank = 1
        for j in range(len(mean)):
            if i!=j and mean[i] < mean[j]: rank+=1
        answer.append(rank)
        
    return answer