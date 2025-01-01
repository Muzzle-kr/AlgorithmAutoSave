function solution(answers) {
  var answer = [];
  const a = [1, 2, 3, 4, 5];
  const b = [2, 1, 2, 3, 2, 4, 2, 5];
  const c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  
  const supoja1Count = answers.filter((answer, i) => answer === a[i%a.length]).length;
  const supoja2Count = answers.filter((answer, i) => answer === b[i%b.length]).length;
  const supoja3Count = answers.filter((answer, i) => answer === c[i%c.length]).length;
  
  let maxCount = Math.max(supoja1Count, supoja2Count, supoja3Count);
  
  if(supoja1Count === maxCount) answer.push(1);
  if(supoja2Count === maxCount) answer.push(2);
  if(supoja3Count === maxCount) answer.push(3);
  
  return answer;
}