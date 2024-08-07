#!/usr/bin/node
/**
 * this code will help to point of all character
 * in the specified movie id
 * the movie id is passed as an argument
 * the code will return the name of all characters
 * */
// this line will help to import the request module
const request = require('request');

// this line will help to get the movie id from the command line
const movieId = process.argv[2];
// this line will help to get the url of the movie
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
// this function will help to get the movie info by passing the url
const getMoviesInfo = (url) => {
  // this line will help to return a promise to get the data
  return new Promise((resolve, reject) => {
    // this line will help to get the data from the url
    request(url, (error, Response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

// this function will help to get the character name by passing the character url
const getCharacter = (characterurl) => {
  // this line will help to return a promise to get the character name
  return new Promise((resolve, reject) => {
    // this line will help to get the data from the character url
    request(characterurl, (error, Response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
};
// this function will help to get the character name by passing the url
/**
 * i used async and await to get the character name
 * by passing the url of the movie then i get the data
 * from the movie and then i get the character url
 * then i get the character name by passing the character url
 * then i print the character name
 */
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
