function solution(arr, flag) {
    var answer = [];
    return flag.reduce((a, c, idx) => {
        if (c) {
            for(let i=0;i<arr[idx]*2;i++) a.push(arr[idx])
        } else {
            a = a.slice(0,a.length-arr[idx])
        }
        return a;
    }, []);
}