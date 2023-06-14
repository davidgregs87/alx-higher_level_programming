#!/usr/bin/node
const arrLen = process.argv.length;
const arrVal = process.argv[2];
if (arrLen === 2) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arrVal; i++) {
    console.log('C is fun');
  }
}
