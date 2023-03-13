#!/usr/bin/node

const size = process.argv.length;
let squareSize;
const pattern = 'X';

if (size === 2 || isNaN(process.argv[2])) {
  console.log('Missing size');
} else if (size >= 3 && !isNaN(process.argv[2])) {
  squareSize = parseInt(process.argv[2]);
  for (let i = 0; i < squareSize; i++) {
    console.log(pattern.repeat(squareSize));
  }
}
