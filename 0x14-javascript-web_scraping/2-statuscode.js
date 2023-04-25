#!/usr/bin/node

const request = require('request');
const argv = process.argv;

request(argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
