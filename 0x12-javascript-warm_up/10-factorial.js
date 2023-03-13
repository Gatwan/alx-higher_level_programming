#!/usr/bin/node
function factorial (a) {
  if ((isNaN(a)) || (a === 1)) {
    return 1;
  }
  return factorial(a - 1) * a;
}
console.log(factorial(parseInt(process.argv[2])));
