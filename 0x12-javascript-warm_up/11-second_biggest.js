#!/usr/bin/node

const size = process.argv.length;
const myVar = [];

if (size === 2 || size === 3) {
  console.log(0);
} else if (size >= 3) {
  for (let i = 2; i < size; i++) {
    myVar.push(process.argv[i]);
  }
}

if (myVar.length > 1) {
  myVar.sort(function (a, b) {
    return a - b;
  });
  console.log(myVar[myVar.length - 2]);
}
