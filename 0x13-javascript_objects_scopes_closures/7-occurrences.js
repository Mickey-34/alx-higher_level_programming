#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let R = 0;

  for (let m = 0; m <= list.length; m++) {
    if (list[m] === searchElement) {
      R++;
    }
  }
  return R;
};
