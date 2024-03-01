function solution(lines) {
    var answer = 0;
    
    const arr = new Array(201).fill(0)
    
    for(l of lines){
        let [left,right] = l
        left+=100
        right+=100
        for(let i=left;i<right;i++) arr[i]++
    }
    
    for(n of arr){
        if(n>1) answer++
    }
    
    return answer;
}