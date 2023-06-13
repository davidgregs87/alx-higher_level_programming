#!/usr/bin/node
const argVal = process.argv;
if (!argVal[2]) {
  console.log('No argument');
} else {
  console.log(argVal[2]);
}
