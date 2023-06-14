#!/usr/bin/node
const arr = process.argv[2];
if (isNaN(arr)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(arr));
}
