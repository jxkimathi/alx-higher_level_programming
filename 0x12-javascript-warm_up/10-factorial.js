#!/usr/bin/node
function factorial(a) {
  if (a < 0) {
    return (-1);
  }
  if ((a === 0) || isNaN(a)) {
    return (1);
  }
  return (n * factorial(n - 1));
}

console.log(factorial(Number(process.argv[2])));