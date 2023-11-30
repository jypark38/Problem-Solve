def solution(array, n):
    answer = 0
    array.sort()
    _array = [abs(i-n) for i in array]

    
    return array[_array.index(min(_array))]