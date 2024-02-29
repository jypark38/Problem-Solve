function solution(arr, queries) {
    var answer = [];
    queries.forEach(q=>{
        const [s,e,k] = q
        let result = Infinity
        for(let i=s;i<=e;i++){
            if (arr[i]>k && arr[i]<result){
                result = arr[i]   
            }
        }
        if (result===Infinity) result = -1
        answer.push(result)
    })
    return answer;
}