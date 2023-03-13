#!/usr/bin/node
const argv = process.argv;
argv.splice(0, 2);
if (argv.length === 0) {
  console.log(0);
} else {
  argv.sort((a, b) => a - b);
  console.log(+argv[argv.length - 2]);
}
