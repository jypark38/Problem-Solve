function solution(arr, queries) {
    var answer = [];
    for(q of queries){
        [arr[q[0]],arr[q[1]]] = [arr[q[1]],arr[q[0]]]
    }
    return arr;
}