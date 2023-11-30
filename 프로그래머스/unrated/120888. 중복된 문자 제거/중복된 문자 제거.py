def solution(my_string):
    answer = ''
    
    for c in my_string:
        if not c in answer:
            answer += c
    return answer
    