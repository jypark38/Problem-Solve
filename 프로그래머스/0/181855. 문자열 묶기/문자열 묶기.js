function solution(strArr) {
    var answer = 0;
    const arr = Array(31).fill(0)
    let max = 0
    for(c of strArr){
        const l = c.length
        arr[l]++
        if(arr[l]>max) max=arr[l]
    }
    return max;
}