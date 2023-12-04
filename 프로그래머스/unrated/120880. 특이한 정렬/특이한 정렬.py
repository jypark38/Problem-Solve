def solution(numlist, n):
    answer = []
    _n = sorted(numlist,key=lambda x:[abs(x-n),-x])
    return _n