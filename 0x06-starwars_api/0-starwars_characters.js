#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
const getMoviesInfo = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, Response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

const getCharacter = (characterurl) => {
  return new Promise((resolve, reject) => {
    request(characterurl, (error, Response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
};

async function getCharacterName (url) {
  try {
    const data = await getMoviesInfo(url);
    for (let i = 0; i < data.characters.length; i++) {
      const character = await getCharacter(data.characters[i]);
      console.log(character);
    }
  } catch (error) {
    console.log(error);
  }
}
getCharacterName(url);
