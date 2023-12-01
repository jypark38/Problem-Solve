def solution(chicken):
    answer = 0
    order = chicken
    while order>=10:
        answer += order // 10
        order = order // 10 + order %10
    return answer