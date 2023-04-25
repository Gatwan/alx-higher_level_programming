#!/usr/bin/node

const request = require('request');
const argv = process.argv;

request(argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  let count = 0;
  const movies = JSON.parse(body).results;

  for (const movie of movies) {
    const characters = movie.characters;
    for (const character of characters) {
      const characterID = String(character).split('/')[5];
      if (characterID === '18') {
        count++;
      }
    }
  }
  console.log(count);
});
