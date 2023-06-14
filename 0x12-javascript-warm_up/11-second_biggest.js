#!/usr/bin/node
const argVal = process.argv.length;
const arr = process.argv;
if (!arr[2]) {
  console.log(0);
} else if (argVal === 3) {
  console.log(0);
} else {
  const num = arr.slice(2);
  const sortNum = num.sort((a, b) => b - a);
  const result = sortNum[1];
  console.log(result);
}
