function solution(arr, queries) {
    for(q of queries){
        const [s,e] = q
        for(let i = s; i<=e;i++){
            arr[i]+=1
        }
    }
    return arr;
}