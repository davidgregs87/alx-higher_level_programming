#!/usr/bin/node
const arrVal = parseInt(process.argv[2]);
function fact (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  } else {
    return (num * fact(num - 1));
  }
}
const res = fact(arrVal);
console.log(res);
