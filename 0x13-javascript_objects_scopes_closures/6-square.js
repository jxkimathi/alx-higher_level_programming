#!/usr/bin/node
const Squarep = require('./5-square');

class Square extends Squarep {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let j = 0; j < this.width; j++) {
        x += c;
      }
      console.log(x);
    }
  }
}

module.exports = Square;
