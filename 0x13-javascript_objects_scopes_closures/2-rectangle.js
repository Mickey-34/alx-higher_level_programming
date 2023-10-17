#!/usr/bin/node
module.exports = class Rectangle {
  constructor (o, y) {
    if (o > 0 && y > 0) {
      this.width = o;
      this.height = y;
    }
  }
};
