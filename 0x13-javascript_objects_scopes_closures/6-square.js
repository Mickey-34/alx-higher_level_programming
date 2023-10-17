#!/usr/bin/node
// Definition of a square (a square is a square)
const _Square = require('./5-square');
module.exports = class Square extends _Square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let m = 0; m < this.height; m++) {
      console.log(c.repeat(this.width));
    }
  }
};
