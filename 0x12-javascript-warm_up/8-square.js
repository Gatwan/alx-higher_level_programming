#!/usr/bin/node
const size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0, s; i < size; i++) {
    s = '';
    for (let j = 0; j < size; j++) {
      s += 'X';
    }
    console.log(s);
  }
}
