#!/usr/bin/node
const arrLen = process.argv.length;
const arrVal = process.argv[2];
if (arrLen === 2) {
  console.log('Missing size');
} else if (isNaN(arrVal)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arrVal; i++) {
    console.log('X'.repeat(arrVal));
  }
}
