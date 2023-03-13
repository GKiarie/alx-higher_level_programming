#!/usr/bin/node

const size = process.argv.length;

if (size === 2) {
  console.log('No argument');
} else if (size > 2) {
  console.log(process.argv[2]);
}
