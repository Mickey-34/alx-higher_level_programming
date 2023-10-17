#!/usr/bin/node
const MyVar = process.argv[2];
if (isNaN(MyVar) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let m = 0; m < MyVar; m++) {
    console.log('C is fun');
  }
}
