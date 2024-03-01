function solution(friends, gifts) {
    var answer = {};
    
    const score={}
    const gives={}
    const takes={}
    const table={}
    
    for(let id of friends){
        answer[id] = 0
        gives[id]=[]
        takes[id]=[]
        table[id]={}
        friends.forEach(e=>{
            table[id][e] = 0
        })
    }
    
    for(let g of gifts){
        let [a,b] = g.split(' ')
        gives[a].push(b)
        takes[b].push(a)
        table[a][b]+=1
    }
    
    for(let id of friends){
        score[id] = gives[id].length - takes[id].length
    }
    for(let i=0;i<friends.length;i++){
        for(let j=0;j<friends.length;j++){
            if(i==j) continue
            const n1 = friends[i]
            const n2 = friends[j]
            
            if(table[n1][n2]>table[n2][n1]){
                answer[n1]+=1
            }
            if(table[n1][n2]==table[n2][n1]){
                if(score[n1]>score[n2]){
                    answer[n1]+=1
                }
            }
        }
        
    }
    
    return Math.max(...Object.values(answer));
}