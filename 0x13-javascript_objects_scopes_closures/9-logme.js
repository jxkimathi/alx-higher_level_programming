#!/usr/bin/node
let nar = 0;

exports.logMe = function (item) {
  console.log(nar + ': ' + item);
  nar++;
};
