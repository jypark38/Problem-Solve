function solution(numbers, target) {
    var answer = 0;
    
    const dfs = (numbers, target, i, v) => {
        if(i===numbers.length){
            if(v===target){
                answer+=1
            }
            return
        }
        dfs(numbers, target, i+1,v+numbers[i])
        dfs(numbers, target, i+1,v-numbers[i])
    }
    
    dfs(numbers,target,0,0)
    
    return answer;
}