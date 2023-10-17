#!/usr/bin/node
exports.callMeMoby = function (num, theFunction) {
  for (let m = 0; m < num; m++) {
    theFunction();
  }
};
