function solution(date1, date2) {
    var answer = 0;
    const d1 = new Date(date1.join('-'))
    const d2 = new Date(date2.join('-'))
    return (d1<d2)*1;
}