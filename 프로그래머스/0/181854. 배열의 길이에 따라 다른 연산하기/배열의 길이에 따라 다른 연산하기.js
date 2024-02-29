function solution(arr, n) {
    return arr.length % 2 ? arr.map((e,i)=> i%2 ? e : e+n): arr.map((e,i)=> i%2 ? e+n : e)
}