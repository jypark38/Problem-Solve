function solution(num_list) {
    const a = num_list.filter(e=>e%2).reduce((a,b)=>a+b,'')
    const b = num_list.filter(e=>e%2==0).reduce((a,b)=>a+b,'')
    return a*1+b*1
}