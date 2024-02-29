function solution(ineq, eq, n, m) {
    if(ineq==='<'){
        if(eq==='='){
            return (n<=m) * 1
        }
        return (n<m )* 1
    }
    if(ineq==='>'){
        if(eq==='='){
            return (n>=m) * 1
        }
        return (n>m) * 1
    }
}