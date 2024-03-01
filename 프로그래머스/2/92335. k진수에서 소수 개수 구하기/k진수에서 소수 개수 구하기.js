function solution(n, k) {
    var answer = 0;
    console.log(n.toString(k))
    let num = n.toString(k)
    const primes = num.split('0').filter(e=>isPrime(e));
    num = num.split('0')

    const l = num.length
    for(let i=0;i<l;i++){
        if(num[i]==0){
            continue
        }
        if(primes.includes(num[i])){
            answer+=1
        }
    }
    
    
    return answer
}

function isPrime(v){
    if(v==1) return false
    
    const end = Math.sqrt(v)
    
    for(let i=2;i<=end;i++){
        if(v%i == 0){
            return false
        }
    }
    return true
}