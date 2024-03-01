function solution(N, stages) {
    var answer = [];
    const dict = {}
    let person = stages.length
    for(let i =1;i<=N;i++){
        dict[i] = 0
    }
    for(s of stages){
        if(s>=1 && s<=N) dict[s]++
    }
    let entries = Object.entries(dict)
    entries = entries.map((e)=>{
        let fail
        if(person>0){
            fail = e[1]/person
            person -= e[1]
        } else{
            fail = 0
        }
        return [e[0]*1,fail]
    })
    // console.log(entries)
    entries = entries.sort((a,b)=>-a[1]+b[1])
    // console.log(entries)
    return entries.filter(e=>e[0]!=N+1).map(e=>1*e[0]);
}