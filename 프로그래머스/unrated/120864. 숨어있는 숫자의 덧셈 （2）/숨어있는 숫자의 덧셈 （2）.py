def solution(my_string):
    answer = 0
    stack = ''
    for c in my_string:
        if c.isdigit():
            stack += c
        elif len(stack) and not c.isdigit():
            answer += int(stack)
            stack = ''
    if len(stack):
        answer += int(stack)
    return answer
