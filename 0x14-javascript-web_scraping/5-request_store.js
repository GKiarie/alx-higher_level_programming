#!/usr/bin/node
// script that gets the contents of a webpage
// stores it in a file
const request = require('request');
const fs = require('fs');

request(process.argv[2], (error, response, body) => {
  if (error) console.log(error);
  fs.writeFile(process.argv[3], body, error => {
    if (error) console.log(error);
  });
});
