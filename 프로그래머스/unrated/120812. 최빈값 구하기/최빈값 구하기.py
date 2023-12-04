def solution(array):
    cnt = list(map(lambda x:array.count(x),set(array)))
    if cnt.count(max(cnt))>1: return -1
    answer = sorted(array,key=lambda x:array.count(x))[-1]
    
    
    return answer