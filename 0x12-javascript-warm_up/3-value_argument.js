#!/usr/bin/node
let e = 0;
process.argv.forEach((val, index) => {
  e++;
  if (index === 2) {
    console.log(`${val}`);
  }
});
if (e <= 2) {
  console.log('No argument');
}
