function solution(arr, queries) {
    var answer = [];
    for(q of queries){
        const [s,e,k] = q
        for(let i=s;i<=e;i++){
            if(i%k==0) arr[i]+=1
        }
    }
    return arr;
}