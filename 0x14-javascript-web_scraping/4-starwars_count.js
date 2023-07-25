#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else {
    const film = JSON.parse(body).results;
    let count = 0;
    for (const x in film) {
      const character = film[x].characters;
      for (const item in character) {
        if (character[item].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
