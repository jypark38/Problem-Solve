def solution(my_string):
    return [int(i) for i in sorted(my_string) if i.isdigit()]