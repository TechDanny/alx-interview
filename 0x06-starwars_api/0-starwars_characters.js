#!/usr/bin/env node

const request = require('request');

const movieId = process.argv[2];
const filmEndPoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let persons = [];
const name = [];

const requestChar = async () => {
  await new Promise(resolve => request(filmEndPoint, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      console.error('Error: ', err, '| StatusCode: ', res.statusCode);
    } else {
      const Body = JSON.parse(body);
      persons = Body.characters;
      resolve();
    }
  }));
};

const requestPersons = async () => {
  if (persons.length > 0) {
    for (const x of persons) {
      await new Promise(resolve => request(x, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          console.error('Error: ', err, '| StatusCode: ', res.statusCode);
        } else {
          const Body = JSON.parse(body);
          name.push(Body.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: Characters missing');
  }
};

const getNames = async () => {
  await requestChar();
  await requestPersons();

  for (const x of name) {
    if (x === name[name.length - 1]) {
      process.stdout.write(x + '\n');
    } else {
      process.stdout.write(x + '\n');
    }
  }
};

getNames();
