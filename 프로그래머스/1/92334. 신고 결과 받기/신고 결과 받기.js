function solution(id_list, report, k) {
    var answer = {};
    report = Array.from(new Set(report))
    const reports = {}
    const fromReport = {}
    let bans
    id_list.forEach(e=>{
        reports[e] = 0
        answer[e] = 0
        fromReport[e] = []
    })
    
    report.forEach(e=>{
        const [a,b] = e.split(' ')
        reports[b]+=1
        fromReport[b].push(a)
    })
    
    bans = Object.entries(reports).filter(e=>e[1]>=k).map(e=>e[0])
    
    bans.forEach(e=>{
        const p = fromReport[e]
        p.forEach(e2=>{
            answer[e2]+=1
        })
    })
    
    return Object.values(answer);
}