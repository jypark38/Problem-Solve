def solution(quiz):
    answer = []
    for q in quiz:
        _q = q.split(' = ')
        r = _q[0]
        a = int(_q[1])
        if ' - ' in r:
            A = int(r.split(' - ')[0]) - int(r.split(' - ')[1])
        elif ' + ' in r:
            A = int(r.split(' + ')[0]) + int(r.split(' + ')[1])
        if a == A: answer.append('O')
        else: answer.append('X')
    return answer