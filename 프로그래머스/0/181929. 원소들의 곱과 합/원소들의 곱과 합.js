function solution(num_list) {
    const m = num_list.reduce((a,b)=>a*b)
    const s = num_list.reduce((a,b)=>a+b)**2
    return m>s ? 0 : 1;
}