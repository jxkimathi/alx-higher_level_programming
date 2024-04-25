#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${episode}`;

request(URL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
