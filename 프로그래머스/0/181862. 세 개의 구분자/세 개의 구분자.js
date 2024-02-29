function solution(myStr) {
    var answer = [];
    myStr=myStr.replaceAll('a','-')
    myStr=myStr.replaceAll('b','-')
    myStr=myStr.replaceAll('c','-')
    answer = myStr.split('-').filter(e=>e.length)
    return answer.length ? answer : ['EMPTY'];
}