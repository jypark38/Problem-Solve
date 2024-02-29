function solution(arr, queries) {
    var answer = [];
    for(q of queries){
        const [a,b] = q
        let temp = arr[b]
        arr[b] = arr[a]
        arr[a] = temp
    }
    return arr;
}