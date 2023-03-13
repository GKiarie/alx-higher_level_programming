#!/usr/bin/node

const size = process.argv.length;
let firstArg = process.argv[2];

if (size >= 3) {
  if (!isNaN(firstArg)) {
    firstArg = parseInt(firstArg);
    console.log(`My number: ${firstArg}`);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
