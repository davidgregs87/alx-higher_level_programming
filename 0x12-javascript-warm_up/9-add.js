#!/usr/bin/node
const arrLen = process.argv.length;
const arrVal = process.argv;
const arrVal1 = parseInt(arrVal[2]);
const arrVal2 = parseInt(arrVal[3]);
if (arrLen === 2) {
  console.log('NaN');
} else if (arrLen === 3) {
  console.log('NaN');
} else {
  function add (a, b) {
    return a + b;
  }
  console.log(add(arrVal1, arrVal2));
}
