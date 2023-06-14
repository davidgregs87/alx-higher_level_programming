#!/usr/bin/node
const myArg = process.argv;
myArg[0] = 'undefined';
myArg[1] = 'undefined';
if (!myArg[2]) {
  console.log(myArg[0] + ' is ' + myArg[1]);
} else if (myArg === 2) {
  console.log(myArg[2] + ' is ' + myArg[1]);
} else {
  console.log(myArg[2] + ' is ' + myArg[3]);
}
