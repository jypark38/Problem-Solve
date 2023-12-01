def solution(dots):
    answer = 0
    
    dot = dots[0]
    dots.remove(dot)
    
    for d in dots:
        if d[0] == dot[0]: h = abs(dot[1]-d[1])
        if d[1] == dot[1]: w = abs(dot[0]-d[0])
    
    return w*h