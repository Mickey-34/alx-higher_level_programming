#!/usr/bin/node
exports.esrever = function (list) {
  const newAra = [];
  for (let m = list.length - 1; m >= 0; m--) {
    newAra.push(list[m]);
  }
  return newAra;
};
