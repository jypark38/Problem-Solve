function solution(n, k) {
    var answer = 0;
    console.log(n.toString(k))
    let num = n.toString(k)
    const primes = num.split('0').filter(e=>isPrime(e));
    num = num.replaceAll('0','-0-').replaceAll('--','-').split('-')

    const l = num.length
    for(let i=0;i<l;i++){
        if(num[i]==0){
            continue
        }
        if(primes.includes(num[i])){
            if(i==0 || i==l-1){
                if(i==l-1){
                    answer+=1
                }else if(i==0 && num[i+1]==0){
                    answer+=1
                }else if(i==l-1 && num[i-1]==0){
                    answer+=1
                }
            }
            if(i>0 && i<l){
                if(num[i-1]==0 && num[i+1]==0){
                    answer+=1
                }
            }
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