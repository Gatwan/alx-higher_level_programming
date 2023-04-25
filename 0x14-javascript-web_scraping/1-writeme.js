#!/usr/bin/node

const fs = require('fs');
const argv = process.argv;

fs.writeFile(argv[2], argv[3], (err) => {
  if (err) {
    console.error(err);
  }
});
