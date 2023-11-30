def solution(my_string):
    arr = my_string.split()
    answer = int(arr[0])
    
    stack = ''
    for c in arr[1:]:
        if c in '+-':
            stack = c
        else:
            if stack == '+':
                answer += int(c)
            if stack == '-':
                answer -= int(c)
            stack = ''
    return answer