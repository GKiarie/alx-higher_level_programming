#!/usr/bin/node
// script that prints the number of movies
// where the character 'Wedge Antilles' is present

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) console.log(error);
  let count = 0;
  for (let i = 0; i < JSON.parse(body).results.length; i++) {
    const chars = JSON.parse(body).results[i].characters;
    for (let j = 0; j < chars.length; j++) {
      if (chars[j].includes('18')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
