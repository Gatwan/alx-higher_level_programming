#!/usr/bin/node
const num = (process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
}
for (let x = 0; x < num; x++) {
  console.log('C is fun');
}
