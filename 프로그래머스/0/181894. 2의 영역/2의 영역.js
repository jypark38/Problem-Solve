function solution(arr) {
    var answer = [];
    let s;
    let e;
    for(i=0;i<arr.length;i++){
        if(arr[i]==2){
            s=i
            break
        }
    }
    for(i=arr.length-1;i>=0;i--){
        if(arr[i]==2){
            e=i
            break
        }
    }
    answer = arr.slice(s,e+1)
    
    return answer.length?answer:[-1];
}