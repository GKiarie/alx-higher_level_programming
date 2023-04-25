#!/usr/bin/node
// script that prints the title of a Star Wars movie
// where the episode number matches a given integer

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + process.argv[2], (error, response, body) => {
  console.log(error || JSON.parse(body).title);
});
