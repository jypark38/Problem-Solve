function solution(arr1, arr2) {
    var answer = 0;
    if (arr1.length > arr2.length) return 1
    if (arr1.length < arr2.length) return -1
    
    const s1 = arr1.reduce((a,b)=>a+b)
    const s2 = arr2.reduce((a,b)=>a+b)
    
    if(s1>s2) return 1
    if(s1<s2) return -1
    
    return 0;
}