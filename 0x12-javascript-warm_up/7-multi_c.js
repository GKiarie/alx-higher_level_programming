#!/usr/bin/node

if (process.argv.length === 2) {
  console.log('Missing number of occurences');
} else if (process.argv.length >= 3) {
  const numOccurences = parseInt(process.argv[2]);
  for (let i = 0; i < numOccurences; i++) {
    console.log('C is fun');
  }
}
