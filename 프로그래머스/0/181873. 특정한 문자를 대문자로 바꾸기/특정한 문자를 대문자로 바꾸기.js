function solution(my_string, alp) {
    const a = alp.toUpperCase()
    return my_string.replaceAll(alp,a);
}