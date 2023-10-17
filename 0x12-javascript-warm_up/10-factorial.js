#!/usr/bin/node

function factorialize (num) {
  let MyRes = 1;
  for (let m = 1; m <= num; m++) {
    MyRes *= m;
  }
  return (MyRes);
}
console.log(factorialize(parseInt(process.argv[2])));
