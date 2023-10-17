#!/usr/bin/node
let e = 0;
process.argv.forEach((_val, _index) => {
  e++;
});
if (e <= 2) {
  console.log('No argument');
} else if (e === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
