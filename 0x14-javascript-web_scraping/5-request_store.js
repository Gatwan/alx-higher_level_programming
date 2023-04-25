#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const argv = process.argv;

request(argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  fs.writeFile(argv[3], body, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
