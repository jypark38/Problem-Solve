function check(user, ban){
    if(user.length !== ban.length){
        return false
    }
    for (let i=0;i<user.length;i++){
        if(user[i] !== ban[i] && ban[i] !== '*'){
            return false
        }
    }
    return true
}



function solution(user_id, banned_id) {
    var answer = 0;
    const set = new Set();
    const visited = Array(user_id.length).fill(false);
    
    const dfs = (idx=0, arr=[]) => {
        if(idx === banned_id.length){
            set.add(arr.sort().join(' '))
        } else{
            for(let i=0; i<user_id.length;i++){
                if(visited[i]){
                    continue
                }
                if(check(user_id[i],banned_id[idx])){
                    visited[i] = true;
                    dfs(idx+1, [...arr,user_id[i]])
                    visited[i] = false
                }
            }
        }
    }
    dfs()
    
    answer = set.size
    return answer;
}