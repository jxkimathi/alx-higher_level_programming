#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (const i = 0; i < x; i++) theFunction();
};
