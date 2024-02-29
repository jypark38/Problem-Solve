function solution(num_list) {
    const {m,s} = num_list.reduce(({m,s},c) => {
        m*=c
        s+=c
        return {m, s};
    },{m:1,s:0})
    return m>s**2 ? 0 : 1;
}