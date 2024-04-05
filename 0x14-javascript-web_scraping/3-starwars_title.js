#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const URL = 'https://swapi-api.alx-tools.com/api/films/';

request(URL + episode, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
