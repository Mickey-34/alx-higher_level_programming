#!/usr/bin/node
module.exports = class Rectangle {
  constructor (o, y) {
    if (o > 0 && y > 0) {
      this.width = o;
      this.height = y;
    }
  }

  print () {
    let B = '';
    for (let m = 0; m < this.width; m++) {
      B += 'X';
    }
    for (let m = 0; m < this.height; m++) {
      console.log(B);
    }
  }

  rotate () {
    const aux = this.height;
    this.height = this.width;
    this.width = aux;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
